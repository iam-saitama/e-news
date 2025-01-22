from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/<int:pk>/', views.news_page, name='news_page'),
    path('category/<int:pk>/', views.category_page, name='category_page'),
    path('categories/', views.category_list, name='category_list'),
]