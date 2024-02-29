from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия пользователя')
    email = models.EmailField(unique=True, verbose_name='адрес электронной почты')
    avatar = models.ImageField(upload_to='users/', default='users/avatar_default.jpeg', verbose_name='аватар',
                               **NULLABLE)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name}, {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
