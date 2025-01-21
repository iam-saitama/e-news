from django.db import models

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
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.title
