# Create your models here.

from django.db import models
import datetime


class TableInTarget(models.Model):
    tt_number = models.CharField('Номер КИ', max_length=20, default='1')
    MRF_name  = models.CharField('Регион', max_length=10, default='пусто')
    cr_date_tt = models.DateTimeField('Дата создания КИ', default=datetime.datetime.now())
    name_verifiable = models.CharField('ФИО проверяемого', max_length=50, default='пусто')
    name_verifiable_sheff = models.CharField('ФИО руководителя', max_length=50, default='пусто')
    division_verifiable = models.CharField('Подразделение проверяемого', max_length=50, default='пусто')
    target_type = models.CharField('Таргет проверки', max_length=50, default='пусто')
    kk_result = models.CharField('Результат проверки', max_length=50, default='пусто')


# from main.models import User


# def create_user(username, email):
#     user = User.objects.create(username=username, email=email)
#     # Можно также добавить другие поля пользователя здесь, если они есть
#     user.save()

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
    # Добавьте другие поля, необходимые для вашей модели пользователя

    # def __str__(self):
    #     return self.username


# class News:
#     def __init__(self, tittle, text, date):
#         self.tittle = tittle
#         self.text = text
#         self.date = date
#
#     def __str__(self):
#         return f'{self.tittle}: {self.text}, {self.date}'
#
#
# class Product:
#     counter = 0
#
#     def __init__(self, title, price, quantity):
#         self.title = title
#         self.price = price
#         self.quantity = quantity
#         Product.counter += 1
#
#     def amount(self):
#         return self.price * self.quantity
