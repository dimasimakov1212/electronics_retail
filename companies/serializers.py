from rest_framework import serializers

from companies.models import Company
from companies.validators import validator_company_creation


class CompanyCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Company """

    class Meta:
        model = Company
        exclude = ('company_date_creation',)
        # fields = '__all__'

        # валидаторы на правильность заполнения полей объекта
        validators = [
            validator_company_creation,
        ]


class CompanySerializer(serializers.ModelSerializer):
    """ Сериализатор для списка компаний """

    class Meta:
        model = Company
        fields = '__all__'


class CompanyUpdateSerializer(serializers.ModelSerializer):
    """ Сериализатор для изменения компании """

    class Meta:
        model = Company
        exclude = ('debt_to_supplier',)
