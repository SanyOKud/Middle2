from django.shortcuts import render

from django.http import HttpResponse

from .models import News


def index(request):
    value = -10
    n1 = News('Новость 1', 'Текст 1', '11.11.23')
    n2 = News('Новость 2', 'Текст 2', '12.11.23')
    l = [n1, n2]
    context = {'title': 'Страница главная',
                        'Header1': 'Заголовок страницы',
               'value': value,
               'numbers': l}
    return render(request, 'main/index.html', context)


# Create your views here.

# Страницы ручные #

#def index(request):
   #return HttpResponse('<h1> Главная страница </h1>')

def about(request):
   return HttpResponse('<h1> страница про нас </h1>')

def contacts(request):
   return HttpResponse('<h1> контакт </h1>')

