from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name   = models.CharField(max_length=100)
    slug           = models.SlugField(max_length=100, unique=True)
    category_images = models.ImageField(upload_to = 'category')

    class Meta:
        verbose_name = 'Danh mục sản phẩm'
        verbose_name_plural = 'Danh mục sản phẩm'

    def get_absolute_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name