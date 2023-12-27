from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from companies.models import Company
from companies.paginators import CompanyPaginator
from companies.serializers import CompanyCreateSerializer, CompanySerializer, CompanyUpdateSerializer
from users.permissions import IsActive


class CompanyCreateAPIView(generics.CreateAPIView):
    """ Создание компании """

    serializer_class = CompanyCreateSerializer

    permission_classes = [IsActive]

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """

        new_company = serializer.save()
        new_company.save()


class CompanyListAPIView(generics.ListAPIView):
    """ Вывод списка компаний """

    serializer_class = CompanySerializer
    pagination_class = CompanyPaginator  # пагинация

    permission_classes = [IsActive]

    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('company_country',)
    ordering_fields = ['company_country']

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Company.objects.all()
        return queryset


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр информации об однй компании """

    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    permission_classes = [IsActive]


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """ Изменение компании """

    serializer_class = CompanyUpdateSerializer
    queryset = Company.objects.all()

    permission_classes = [IsActive]


class CompanyDestroyAPIView(generics.DestroyAPIView):
    """ Удаление компании """

    queryset = Company.objects.all()

    permission_classes = [IsActive]
