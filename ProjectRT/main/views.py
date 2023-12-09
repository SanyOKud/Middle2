from django.shortcuts import render

from django.http import HttpResponse

from .models import News, Product


def user_list(request):
    users = User.objects.all()
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'user_list.html', {'users': users, 'form': form})

# def index(request):
#     # value = -10
#     # n1 = News('Новость 1', 'Текст 1', '11.11.23')
#     # n2 = News('Новость 2', 'Текст 2', '12.11.23')
#     # l = [n1, n2]
#     # context = {'title': 'Страница главная',
#     #                     'Header1': 'Заголовок страницы',
#     #            'value': value,
#     #            'numbers': l}
#     if request.method == 'POST':
#         print('Получил ПОСТ-запрос')
#         print(request.POST)
#         title = request.POST.get('title')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         new_product = Product(title, float(price), int(quantity))
#         print('Создан товар:', new_product.title, 'Общая сумма:', new_product.amount())
#     else:
#         print('Получили гет-Запрос!')
#
#     water = Product('Добрый-минералка', 40, 2)
#     chocolate = Product('Баунти', 50, 1)
#
#     colors = ['red', 'blue', 'golden', 'black']
#     context = {
#         'colors' : colors,
#         'water': water,
#         'chocolate': chocolate,
#     }
#     return render(request, 'main/index.html', context)


# Create your views here.

# Страницы ручные #

#def index(request):
   #return HttpResponse('<h1> Главная страница </h1>')

# def get_demo(request, a, operation, b):
#     match operation:
#         case 'plus':
#             result = int(a) + int(b)
#         case 'minus':
#             result = int(a) - int(b)
#         case 'multiply':
#             result = int(a) * int(b)
#         case 'divide':
#             result = int(a) / int(b)
#         case _:
#             return HttpResponse(f'Неверная команда')
#
#     return HttpResponse(f'Вы ввели: {a} и {b} <br>Результат {operation}: {result}')
#
#     return HttpResponse(f'Вы ввели: {a} и {b} <br> Сумма: {a+b}')
#
# def about(request):
#    return HttpResponse('<h1> страница про нас </h1>')
#
# def contacts(request):
#    return HttpResponse('<h1> контакт </h1>')

def custom_404(request, exception):
    return HttpResponse(f'Ой-ёй-ёй! Какая жалость!:{exception}')