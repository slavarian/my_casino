from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator , RegexValidator
import datetime

class MyUser(AbstractBaseUser,PermissionsMixin):
    class Currencies(models.TextChoices):
        TENGE = 'KZT', 'Tenge'
        RUBLI = 'RUB', 'Rubli'
        EURO = 'EUR', 'Euro'
        DOLLAR = 'USD', 'Dollar'
    email = models.EmailField(
        verbose_name='почта/логин',
        max_length=200,
        unique=True
    )
    nickname = models.CharField(
        verbose_name='никнейм',
        max_length=120
    )
    currency = models.CharField(
        verbose_name='валюта',
        max_length=4,
        choices=Currencies.choices,
        default=Currencies.TENGE
    )



    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class ActivationCode(models.Model):
    user = models.OneToOneField(
        verbose_name='пользователь',
        related_name='code',
        to=MyUser,
        on_delete=models.CASCADE
    )
    code = models.CharField(
        verbose_name='код',
        unique=True,
        max_length=200
    )

    is_active = models.BooleanField(
        verbose_name= 'активный?',
        default=True
    )

    card_time = models.DateTimeField(
        verbose_name='дата создания',
        auto_created= True

    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'код'
        verbose_name_plural = 'Код активации'

class BankCard(models.Model):
    card_bank = models.CharField(
        verbose_name='банк карты',
        max_length=120
    )
    card_num = models.IntegerField(
        verbose_name='номер карты',
        max_length=16,
        validators=[
            RegexValidator(regex=r'^\d{16}$', message='не верный номер')
        ]
    )
    card_time = models.DateField(
        verbose_name='срок действия карты',
       
    )
    card_owner = models.OneToOneField(
        verbose_name='владелец карты',
        related_name='card',
        to=MyUser,
        on_delete=models.CASCADE
    )
    card_cvv = models.IntegerField(
        verbose_name='CVV карты',
        max_length=16,
        validators=[
            RegexValidator(regex=r'^\d{3}$', message='не верный номер')
        ]
    )
    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'Банковская карта'
        verbose_name_plural = 'Банковская картаы'

class Transaction:
    user = models.ForeignKey(
        verbose_name='пользователь',
        related_name='transactions',
        to=MyUser,
        on_delete=models.PROTECT

    )
    amount = models.DecimalField(
        verbose_name='сумма',
        max_digits=11,
        decimal_places=2
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата транзации',
        auto_now_add=True
    )
    is_filled = models.BooleanField(
        verbose_name='пополнение?',
        default=False
    )
    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'