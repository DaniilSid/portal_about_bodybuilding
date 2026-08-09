# main/admin.py
from django.contrib import admin
from .models import Category, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Флаг is_featured_on_home можно переключать прямо из списка!
    list_display = ('title', 'category', 'is_featured_on_home', 'created_at')
    list_editable = ('is_featured_on_home',)
    list_filter = ('category', 'is_featured_on_home')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
