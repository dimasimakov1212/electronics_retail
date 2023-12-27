from django.contrib import admin

from companies.models import Company

# admin.site.register(Company)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_city', 'company_type', 'company_supplier', 'debt_to_supplier')
    actions = ['nullify_debt']

    def nullify_debt(self, request, queryset):
        for item in queryset:
            item.debt_to_supplier = 0
            item.save()
        self.message_user(request, f'Задолженность перед поставщиком у выбранных покупателей обнулена.')

    nullify_debt.short_description = 'Обнулить задолженность'
