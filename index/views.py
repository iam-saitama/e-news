from django.shortcuts import render, redirect
from .models import NewsCategory, News
from .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    category = NewsCategory.objects.all()
    news = News.objects.all()
    # Передаем данные на frontend
    context = {'category': category, 'news': news}

    return render(request, 'index/home.html', context)


def category_list(request):
    # Достаем все категории из БД
    category = NewsCategory.objects.all()
    news_list = News.objects.all()
    # Передаем данные на frontend
    context = {'categories': category, 'news_list': news_list}
    return render(request, 'index/category_list.html', context)


# Вывод новости по выбранной категории
def category_page(request, pk):
    # Достаем выбранную категорию
    category = NewsCategory.objects.get(id=pk)
    # Фильтруем новости по категории
    news = News.objects.filter(category=category)
    # Данные для сайдбара
    news_list = News.objects.all()
    categories = NewsCategory.objects.all()
    # Передаем данные на frontend
    context = {'category': category, 'news': news, 'news_list': news_list, 'categories': categories}

    return render(request, 'index/category.html', context)


# Вывод определенной новости
def news_page(request, pk):
    # Вывод выбранной новости
    news = News.objects.get(id=pk)
    # Данные для сайдбара
    news_list = News.objects.all()
    categories = NewsCategory.objects.all()
    # Передаем данные на frontend
    context = {'news': news, 'news_list': news_list, 'categories': categories}

    return render(request, 'index/news.html', context)


# Регистрация
class Register(View):
    template_name = 'registration/register.html'

    # Выдача формы
    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    # Получение ифны с формы
    def post(self, request):
        form = RegForm(request.POST)

        # Если данные корректны
        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            # Объект класса User
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()

            # Авторизуем пользователя
            login(request, user)
            return redirect('/')
        # Если данные некорректны
        context = {'form': RegForm, 'message': 'Пароль или почта неверны!'}
        return render(request, self.template_name, context)




















