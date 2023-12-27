from django.contrib import admin

from django.utils.html import format_html

from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_city', 'company_type', 'supplier_url',
                    'debt_to_supplier')
    list_filter = ('company_city',)
    actions = ['nullify_debt']

    def nullify_debt(self, request, queryset):
        for item in queryset:
            item.debt_to_supplier = 0
            item.save()
        self.message_user(request, f'Задолженность перед поставщиком у выбранных покупателей обнулена.')

    nullify_debt.short_description = 'Обнулить задолженность'

    def supplier_url(self, obj):
        """ Получение ссылки на поставщика """

        supplier = obj.company_supplier  # получаем поставщика
        try:
            supplier_id = supplier.id
            url = f'{supplier_id}/change/'  # формируем адрес
            return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.company_supplier)
        except AttributeError:
            pass

    supplier_url.short_description = 'Поставщик'
