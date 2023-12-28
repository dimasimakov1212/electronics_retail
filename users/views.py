from rest_framework import generics


from users.models import User
from users.permissions import IsActive
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя """

    serializer_class = UserSerializer

    permission_classes = [IsActive]


class UserListAPIView(generics.ListAPIView):
    """ Вывод списка пользователей """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsActive]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsActive]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Изменение пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [IsActive]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """

    queryset = User.objects.all()

    permission_classes = [IsActive]
