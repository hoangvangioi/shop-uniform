from django.db import models
from category.models import Category
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import unique_slug_generator
from django.db.models.signals import pre_save


# Create your models here.


class Product(models.Model):
	product_name    = models.CharField(max_length=200, unique=True)
	slug            = models.SlugField(max_length=200, unique=True)
	price           = models.IntegerField()
	description     = RichTextUploadingField(blank=True)
	product_images  = models.ImageField(upload_to='products')
	stock           = models.IntegerField()
	is_available    = models.BooleanField(default=True)
	category        = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_date    = models.DateTimeField(auto_now_add=True)
	modified_date   = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name = 'Sản phẩm'
		verbose_name_plural = 'Sản phẩm'


class VariationManager(models.Manager):
	def colors(self):
		return super(VariationManager, self).filter(variation_category='color', is_active=True)

	def sizes(self):
		return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
	('color', 'color'),
	('size', 'size'),
)


class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	variation_category = models.CharField(max_length=100, choices=variation_category_choice)
	variation_value     = models.CharField(max_length=100)
	is_active           = models.BooleanField(default=True)
	created_date        = models.DateTimeField(auto_now=True)

	objects = VariationManager()

	def __str__(self):
		return self.variation_value
	class Meta:
		verbose_name = 'Thuộc tính sản phẩm'
		verbose_name_plural = 'Thuộc tính sản phẩm'
  
  
class ProductGallery(models.Model):
	product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products', max_length=255)

	def __str__(self):
		return self.product.product_name

	class Meta:
		verbose_name = 'Hình ảnh sản phẩm'
		verbose_name_plural = 'Hình ảnh sản phẩm'



def pre_save_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_category_receiver, sender=Product)