# Generated by Django 2.2.19 on 2022-11-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование товара', max_length=200, verbose_name='Имя')),
                ('description', models.TextField(help_text='Введите описание товара', verbose_name='Описание')),
                ('price', models.PositiveIntegerField(help_text='Введите цену товара', verbose_name='Цена')),
            ],
        ),
    ]
