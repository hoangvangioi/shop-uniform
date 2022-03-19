from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save


# Create your models here.


class Category(models.Model):
    category_name   = models.CharField(max_length=100)
    slug           = models.SlugField(max_length=120, unique=True, null=True, blank=True)
    category_images = models.ImageField(upload_to = 'category')

    class Meta:
        verbose_name = 'Danh mục sản phẩm'
        verbose_name_plural = 'Danh mục sản phẩm'

    def get_absolute_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name


def pre_save_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_category_receiver, sender=Category)