# main/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название раздела")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-слаг")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок в меню")

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок статьи")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-слаг")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="Раздел")
    image = models.ImageField(upload_to='articles/', verbose_name="Фото статьи", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, verbose_name="Или прямая ссылка на фото (URL)")
    preview_text = models.TextField(max_length=300, verbose_name="Краткое описание (для плитки)")
    content = RichTextField(verbose_name="Полный текст статьи")
    
    # Флаг для вывода плитки на Главный экран
    is_featured_on_home = models.BooleanField(
        default=False, 
        verbose_name="Показывать плитку на Главном экране"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    # Метод для получения картинки (из файла или ссылки)
    def get_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return "https://via.placeholder.com/600x400?text=Нет+Фото"
