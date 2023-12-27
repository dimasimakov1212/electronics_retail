from django.urls import path

from companies.apps import CompaniesConfig
from companies.views import CompanyCreateAPIView, CompanyListAPIView, CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDestroyAPIView

app_name = CompaniesConfig.name


urlpatterns = [
    path('create/', CompanyCreateAPIView.as_view(), name='company_create'),
    path('list/', CompanyListAPIView.as_view(), name='company_list'),
    path('company/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='company_detail'),
    path('update/<int:pk>/', CompanyUpdateAPIView.as_view(), name='company_change'),
    path('delete/<int:pk>/', CompanyDestroyAPIView.as_view(), name='company_delete'),
]
