from rest_framework.serializers import ValidationError


def validator_company_creation(value):
    """ Проверка на правильность заполнения полей объекта """

    try:
        if value['company_type'] == 'завод':
            if value['company_supplier']:
                raise ValidationError('У завода не может быть поставщика')
    except KeyError:
        pass
