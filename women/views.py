from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from women.models import Women

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
    posts = Women.objects.filter(is_published=1)
    data = {
        'titel': 'главная страница',
        'posts': posts,
        'menu': menu
    }
    return render(request, "women/index.html", context=data, )


def about(request):
    return render(request, 'women/about.html', {'titel': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', data)


def addpage(request):
    return HttpResponse('Дбавление статьи')


def contact(request):
    return HttpResponse('обратная связб')


def login(request):
    return HttpResponse('авторизация')


def show_category(request, cat_id, date_db=None):
    data = {
        'title': 'отображение по рубрикам',
        'menu': menu,
        'posts': date_db,
        'cat_selected': cat_id,
    }

    