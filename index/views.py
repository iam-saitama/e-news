from django.shortcuts import render

from .models import NewsCategory, News

# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    categories = NewsCategory.objects.all()
    news = News.objects.all()
    # Передаем данные на frontend
    contex = {'categories': categories, 'news': news}

    return render(request, 'home.html', contex)