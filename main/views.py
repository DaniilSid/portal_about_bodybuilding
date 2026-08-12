# main/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Article
from django.db.models import Q 
from django.http import JsonResponse

# Главная страница
def home(request):
    # Загружаем только те статьи, у которых стоит галочка "is_featured_on_home"
    featured_articles = Article.objects.filter(is_featured_on_home=True)
    return render(request, 'main/index.html', {
        'featured_articles': featured_articles
    })

# Страница раздела (список плиток раздела)
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()
    return render(request, 'main/category_detail.html', {
        'category': category,
        'articles': articles
    })

# Страница отдельной статьи
def article_detail(request, category_slug, article_slug):
    category = get_object_or_404(Category, slug=category_slug)
    article = get_object_or_404(Article, category=category, slug=article_slug)
    return render(request, 'main/article_detail.html', {
        'category': category,
        'article': article
    })

#Поиск
def search_api(request):
    query = request.GET.get('q', '').strip()
    results = []
    
    if len(query) >= 2:  # Ищем, если введено хотя бы 2 символа
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(preview_text__icontains=query)
        )[:5]  # Берем максимум 5 совпадений для выпадающего списка
        
        for article in articles:
            results.append({
                'title': article.title,
                'category': article.category.name,
                'image': article.get_image(),
                'url': f"/category/{article.category.slug}/{article.slug}/"
            })
            
    return JsonResponse({'results': results})

# Create your views here.
