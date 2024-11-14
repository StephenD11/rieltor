# Generated by Django 5.1.3 on 2024-11-13 07:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('rieltor', '0001_initial'), ('rieltor', '0002_rename_discription_client_description'), ('rieltor', '0003_alter_client_options'), ('rieltor', '0004_alter_client_description_alter_client_email'), ('rieltor', '0005_review_alter_client_created_at_and_more'), ('rieltor', '0006_client_city'), ('rieltor', '0007_alter_review_options_alter_review_comment_and_more'), ('rieltor', '0008_property'), ('rieltor', '0009_alter_property_options_alter_property_bathroom_and_more'), ('rieltor', '0010_alter_property_repair')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('city', models.CharField(blank=True, max_length=20, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ваше имя')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Ваша почта')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Ваша оценка')),
                ('comment', models.TextField(max_length=250, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('square', models.CharField(blank=True, max_length=25, verbose_name='Площадь')),
                ('floor', models.CharField(max_length=3, verbose_name='Этаж')),
                ('price', models.CharField(blank=True, max_length=50, verbose_name='Цена')),
                ('rooms', models.CharField(blank=True, max_length=2, verbose_name='Колличесто комнат')),
                ('living_area', models.CharField(blank=True, max_length=10, verbose_name='Жилая площадь')),
                ('bathroom', models.CharField(blank=True, choices=[('Совмещенный', 'Совмещенный'), ('раздельный', 'раздельный')], default='', max_length=50, verbose_name='Санузел')),
                ('kitchen_area', models.CharField(blank=True, max_length=10, verbose_name='Площадь Кухни')),
                ('city', models.CharField(blank=True, choices=[('Керчь', 'Керчь'), ('Феодосия', 'Феодосия'), ('Симферополь', 'Симферополь')], default='', max_length=25, verbose_name='Города')),
                ('type_of_rooms', models.CharField(blank=True, choices=[('Изолированные', 'Изолированные'), ('Смежные', 'Смежные')], default='', max_length=25, verbose_name='Тип комнат')),
                ('repair', models.CharField(blank=True, choices=[('Косметический', 'Косметический'), ('Евро', 'Евро'), ('Новострой', 'Новострой')], default='', max_length=25, verbose_name='Ремонт')),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимость',
            },
        ),
    ]
