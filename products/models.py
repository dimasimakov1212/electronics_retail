from django.db import models


class Product(models.Model):
    """ Товары """

    product_name = models.CharField(max_length=150, verbose_name='наименование')
    product_model = models.CharField(max_length=150, verbose_name='модель')
    product_release = models.DateField(auto_now=False, auto_now_add=False, verbose_name='дата релиза')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'товары'  # Настройка для наименования набора объектов
        ordering = ('product_name',)  # сортировка
