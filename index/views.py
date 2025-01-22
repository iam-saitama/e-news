from django.shortcuts import render

from .models import NewsCategory, News

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
