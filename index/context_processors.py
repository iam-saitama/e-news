from .models import News


# Последние новости для sidebar'а
def latest_news(request):
    # Получаем последние 5 новостей
    latest_news = News.objects.all().order_by('-created_at')[:6]
    return {'latest_news': latest_news}