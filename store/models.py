from django.db import models
from category.models import Category
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Product(models.Model):
	product_name    = models.CharField(max_length=200, unique=True)
	slug            = models.SlugField(max_length=200, unique=True)
	author          = models.ForeignKey(User, on_delete=models.CASCADE)
	product_details = models.TextField(blank=True)
	description     = RichTextUploadingField(blank=True)
	price           = models.IntegerField()
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
		

# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
# 	avatar = models.ImageField(upload_to='avatar', blank=True)
# 	bio = models.TextField(blank=True)
# 	url_fb = models.URLField(blank=True)
# 	url_instagram = models.URLField(blank=True)
# 	tel = models.CharField(max_length=15, blank=True)
# 	mail = models.EmailField(blank=True)

# 	def __str__(self):
# 		return f'{self.user.first_name} {self.user.last_name}'
