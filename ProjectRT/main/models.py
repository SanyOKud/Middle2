# Create your models here.

from django.db import models

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


class News:
    def __init__(self, tittle, text, date):
        self.tittle = tittle
        self.text = text
        self.date = date

    def __str__(self):
        return f'{self.tittle}: {self.text}, {self.date}'


class Product:
    counter = 0

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity
        Product.counter += 1

    def amount(self):
        return self.price * self.quantity
