from rest_framework import generics

from products.models import Product
from products.paginators import ProductPaginator
from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """ Создание товара """

    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """

        new_product = serializer.save()
        new_product.save()


class ProductListAPIView(generics.ListAPIView):
    """ Вывод списка товаров """

    serializer_class = ProductSerializer
    pagination_class = ProductPaginator  # пагинация

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Product.objects.all()
        return queryset


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр информации об одном товаре """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    """ Изменение товара """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ Удаление товара """

    queryset = Product.objects.all()
