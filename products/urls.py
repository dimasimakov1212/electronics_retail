from django.urls import path

from products.apps import ProductsConfig

app_name = ProductsConfig.name


urlpatterns = [
    # path('create/', UserCreateAPIView.as_view(), name='user_create'),
    # path('', UserListAPIView.as_view(), name='user_list'),
    # path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    # path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_change'),
    # path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
]
