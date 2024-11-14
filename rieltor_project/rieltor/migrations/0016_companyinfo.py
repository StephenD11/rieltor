# Generated by Django 5.1.3 on 2024-11-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0015_alter_property_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название компании')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('whatsup', models.URLField(blank=True, null=True, verbose_name='Ссылка на WhatsUp')),
            ],
            options={
                'verbose_name': 'Информация о компании',
                'verbose_name_plural': 'Информация о компании',
            },
        ),
    ]
