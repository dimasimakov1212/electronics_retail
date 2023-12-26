from django.db import models

from products.models import Product


class Company(models.Model):
    """ Модель компании """

    FACTORY = 'завод'
    RETAILER = 'розница'
    BUSINESSMEN = 'предприниматель'

    COMPANY_CHOICES = (
        (FACTORY, 'завод'),
        (RETAILER, 'розница'),
        (BUSINESSMEN, 'предприниматель')
    )

    company_name = models.CharField(max_length=150, verbose_name='название')
    company_email = models.EmailField(verbose_name='почта')
    company_country = models.CharField(max_length=100, verbose_name='страна')
    company_city = models.CharField(max_length=100, verbose_name='город')
    company_street = models.CharField(max_length=100, verbose_name='улица')
    company_building = models.CharField(max_length=20, verbose_name='дом')
    company_type = models.CharField(max_length=20, choices=COMPANY_CHOICES,
                                    verbose_name='тип компании')
    company_supplier = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                         verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность поставщику')
    company_date_creation = models.DateField(auto_now=False, auto_now_add=True, verbose_name='дата создания')
    company_products = models.ManyToManyField(Product, verbose_name='товары')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.company_name}'

    class Meta:
        verbose_name = 'Компания'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Компании'  # Настройка для наименования набора объектов
        ordering = ('company_name',)  # сортировка
