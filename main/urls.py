# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('category/<slug:category_slug>/<slug:article_slug>/', views.article_detail, name='article_detail'),
    path('api/search/', views.search_api, name='search_api'),
]
