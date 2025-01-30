from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Таблица категорий
class NewsCategory(models.Model):
    title = models.CharField("Название категории", max_length=64)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.title


# Таблица новостей
class News(models.Model):
    title = models.CharField("Заголовок", max_length=512)
    content = models.TextField("Основной текст")
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.title

    def add_to_favorite(self, user):
        FavoriteNews.objects.get_or_create(user=user, news=self)

    def remove_from_favorite(self, user):
        FavoriteNews.objects.filter(user=user, news=self).delete()

    def is_favorite(self, user):
        return FavoriteNews.objects.filter(user=user, news=self).exists()


# Избранные новости
class FavoriteNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'news'], name='unique_favorite_news')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.news.title}"
