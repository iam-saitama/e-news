from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsCategory, News, FavoriteNews
from .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('/')


# Поиск
def search(request):
    query = request.GET.get('q', '').strip()

    if query:
        matching_news = News.objects.filter(title__icontains=query)

        if matching_news.exists():
            return redirect(reverse('news_page', args=[matching_news.first().id]))
        else:
            messages.error(request, f"К сожалению, ничего не найдено по запросу: '{query}'.")
            return redirect(reverse('home_page'))
    else:
        messages.warning(request, "Введите текст для поиска.")
        return redirect(reverse('home_page'))


# Добавление в избранное
@login_required
def add_to_favorites(request):
    if request.method == 'POST':
        news_id = request.POST.get('news_id')
        user = request.user
        news = get_object_or_404(News, id=news_id)

        if not FavoriteNews.objects.filter(user=user, news=news).exists():
            FavoriteNews.objects.create(user=user, news=news)
            messages.success(request, 'Новость добавлена в избранное!')
        else:
            messages.warning(request, 'Эта новость уже в избранном.')

    return redirect(request.META.get("HTTP_REFERER", "/"))


# Удаление из избранного
@login_required
def remove_from_favorites(request):
    if request.method == 'POST':
        news_id = request.POST.get('news_id')
        user = request.user

        deleted = FavoriteNews.objects.filter(user=user, news_id=news_id).delete()
        if deleted[0] > 0:
            messages.success(request, 'Новость удалена из избранного.')
        else:
            messages.warning(request, 'Этой новости не было в избранном.')

    return redirect(request.META.get("HTTP_REFERER", "/"))


# Функция для отображения избранных новостей
@login_required
def view_favorites(request):
    user = request.user
    # Получаем все избранные новости для текущего пользователя
    favorite_news = FavoriteNews.objects.filter(user=user).select_related('news')
    # Передаем их в шаблон
    return render(request, 'index/favorites.html', {'favorite_news': favorite_news})











