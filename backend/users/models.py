from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Q


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    email = models.EmailField(
        max_length=254,
        unique=True)
    username = models.CharField(
        'Username',
        max_length=150,
        unique=True,
        null=False,
        blank=False)
    first_name = models.CharField(
        blank=False,
        verbose_name='Имя',
        max_length=150)
    last_name = models.CharField(
        blank=False,
        verbose_name='Фамилия',
        max_length=150)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Подписан'
    )

    class Meta:
        verbose_name = 'Подписка на авторов'
        verbose_name_plural = 'Подписки на авторов'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscribe'),
            models.CheckConstraint(
                check=~Q(user=F('author')),
                name='self_subscribe'),]

    def __str__(self):
        return f'{self.user.username} - {self.author.username}'
