from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Имя',
        help_text='Введите наименование товара',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание товара',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        help_text='Введите цену товара'
    )