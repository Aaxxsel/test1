from django.http import HttpResponse
from django.shortcuts import render

menu = [
    {'title': 'o сайте', 'url_name': 'about'},
    {'title': 'добавить статью', 'url_name': 'add_page'},
    {'title': 'обратная связь', 'url_name': 'contact'},
    {'title': 'войти', 'url_name': 'login'},
]



data_db = [{'id': 1, 'title': 'Второе значение', 'cobyent': 'третье значение'},
           {'id': 2, 'title': '2 Второе значение', 'cobyent': '2 третье значение'},
           {'id': 3, 'title': '3 Второе значение', 'cobyent': '3 третье значение'}]


def index(request):
    data = {
        'titel': 'главная страница',
        'posts': data_db,
        'menu': menu
    }
    return render(request, "women/index.html", context=data, )


def about(request):
    return render(request, 'women/about.html', {'titel': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse('Дбавление статьи')


def contact(request):
    return HttpResponse('обратная связб')


def login(request):
    return HttpResponse('авторизация')
