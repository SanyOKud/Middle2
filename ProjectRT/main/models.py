from django.db import models

# Create your models here.

class News:
    def __init__(self, tittle,text,date):
        self.tittle = tittle
        self.text = text
        self.date = date

    def __str__(self):
        return f'{self.tittle}: {self.text}, {self.date}'