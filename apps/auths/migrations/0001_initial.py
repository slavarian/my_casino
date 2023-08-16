# Generated by Django 4.2.4 on 2023-08-16 21:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='почта/логин')),
                ('nickname', models.CharField(max_length=120, verbose_name='никнейм')),
                ('currency', models.CharField(choices=[('KZT', 'Tenge'), ('RUB', 'Rubli'), ('EUR', 'Euro'), ('USD', 'Dollar')], default='KZT', max_length=4, verbose_name='валюта')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='BankCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_bank', models.CharField(max_length=120, verbose_name='банк карты')),
                ('card_num', models.IntegerField(max_length=16, validators=[django.core.validators.RegexValidator(message='не верный номер', regex='^\\d{16}$')], verbose_name='номер карты')),
                ('card_time', models.DateField(verbose_name='срок действия карты')),
                ('card_cvv', models.IntegerField(max_length=16, validators=[django.core.validators.RegexValidator(message='не верный номер', regex='^\\d{3}$')], verbose_name='CVV карты')),
                ('card_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL, verbose_name='владелец карты')),
            ],
            options={
                'verbose_name': 'Банковская карта',
                'verbose_name_plural': 'Банковская картаы',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ActivationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_time', models.DateTimeField(auto_created=True, verbose_name='дата создания')),
                ('code', models.CharField(max_length=200, unique=True, verbose_name='код')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный?')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='code', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'код',
                'verbose_name_plural': 'Код активации',
                'ordering': ('-id',),
            },
        ),
    ]
