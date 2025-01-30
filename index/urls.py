from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/<int:pk>/', views.news_page, name='news_page'),
    path('category/<int:pk>/', views.category_page, name='category_page'),
    path('categories/', views.category_list, name='category_list'),
    path('register/', views.Register.as_view(), name='register'),
    path('search/', views.search, name='search'),
    path('favorites/', views.view_favorites, name='view_favorites'),
    path('favorites/add/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/', views.remove_from_favorites, name='remove_from_favorites'),
]