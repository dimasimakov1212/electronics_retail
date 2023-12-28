from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        # создаем тестового пользователя
        self.user = User.objects.create(user_email='admin@sky.pro', is_active=True)
        self.user.set_password('dima123')
        self.user.save()

        # аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_product(self):
        """ Тестирование создания товара """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # задаем данные для создания товара
        data_product = {
            'product_name': 'Test',
            'product_model': 'Test1',
            'product_release': '2024-01-01'
        }

        # создаем товар
        response = self.client.post(
            '/products/create/',
            data=data_product
        )

        # print(response.json())

        # проверяем ответ на создание привычки
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 2, 'product_name': 'Test', 'product_model': 'Test1', 'product_release': '2024-01-01'}
        )

        # проверяем на существование объектов привычек
        self.assertTrue(
            Product.objects.all().exists()
        )

    def test_list_product(self):
        """ Тестирование списка товаров """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовый товар
        Product.objects.create(
            product_name='Test',
            product_model='Test1',
            product_release='2024-01-01'
        )

        # получаем список объектов
        response = self.client.get(
            '/products/list/'
        )

        # print(response.json())

        # проверяем ответ на получение списка привычек
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'id': 5, 'product_name': 'Test',
                          'product_model': 'Test1', 'product_release': '2024-01-01'}]}
        )

    def test_detail_product(self):
        """ Тестирование информации о товаре """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовый товар
        product = Product.objects.create(
            product_name='Test',
            product_model='Test1',
            product_release='2024-01-01'
        )

        # получаем детали товара
        response = self.client.get(
            reverse('products:product_detail', kwargs={'pk': product.pk})
        )

        # print(response.json())

        # проверяем ответ на получение данных
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 4, 'product_name': 'Test', 'product_model': 'Test1', 'product_release': '2024-01-01'}
        )

    def test_change_product(self):
        """ Тестирование изменения товара """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовый товар
        product = Product.objects.create(
            product_name='Test',
            product_model='Test1',
            product_release='2024-01-01'
        )

        # данные для изменения товара
        data_product_change = {
            'product_model': 'Test1_1',
        }

        # получаем детали товара
        response = self.client.patch(
            reverse('products:product_change', kwargs={'pk': product.pk}),
            data=data_product_change
        )

        # print(response.json())

        # проверяем ответ на получение данных
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # проверяем ответ на соответствие сохраненных данных
        self.assertEquals(
            response.json(),
            {'id': 1, 'product_name': 'Test', 'product_model': 'Test1_1', 'product_release': '2024-01-01'}
        )

    def test_delete_product(self):
        """ Тестирование удаления товара """

        # отправляем запрос на аутентификацию пользователя
        response = self.client.post('/users/token/', {"user_email": "admin@sky.pro", "password": "dima123"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # создаем тестовый товар
        product = Product.objects.create(
            product_name='Test',
            product_model='Test1',
            product_release='2024-01-01'
        )

        # удаляем товар
        response = self.client.delete(
            reverse('products:product_delete', kwargs={'pk': product.pk})
        )

        # проверяем ответ на получение привычки
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
