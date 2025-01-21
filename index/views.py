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

    return render(request, 'home.html', context)


# Вывод новости по выбранной категории
def category_page(request, pk):
    # Достаем выбранную категорию
    category = NewsCategory.objects.get(id=pk)
    # Фильтруем новости по категории
    news = News.objects.filter(category=category)
    # Передаем данные на frontend
    context = {'category': category, 'news': news}

    return render(request, 'category.html', context)


# Вывод определенной новости
def news_page(request, pk):
    # Вывод выбранной новости
    news = News.objects.get(id=pk)
    # Передаем данные на frontend
    context = {'news': news}

    return render(request, 'news.html', context)
