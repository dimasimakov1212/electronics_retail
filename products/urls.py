from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, \
    ProductDestroyAPIView

app_name = ProductsConfig.name


urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('list/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_change'),
    path('delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
]
