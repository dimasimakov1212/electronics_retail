from rest_framework import generics


from users.models import User
# from users.permissions import IsOwner, IsSuperuser
from users.serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя """

    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """ Вывод списка пользователей """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    # permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    # permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Изменение пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    # permission_classes = [IsAuthenticated, IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """

    queryset = User.objects.all()

    # permission_classes = [IsAuthenticated, IsOwner | IsSuperuser]

