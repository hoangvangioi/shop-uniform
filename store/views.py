from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from store.forms import ProductForm
from .models import Product, ProductGallery
from category.models import Category
from django.db.models import Q
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.


class ProductListView(ListView):
	model = Product
	template_name = 'store/product_list_form.html'
	context_object_name = 'products'
	ordering = ['-id']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Lists of Product'
		context['head_title'] = 'Lists of Product'
		return context


def store(request, category_slug=None):
	categories = None
	products = None

	if category_slug != None:
		categories = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=categories, is_available=True)
		paginator = Paginator(products, 12)
		page = request.GET.get('page')
		paged_products = paginator.get_page(page)
		product_count = products.count()
	else:
		products = Product.objects.all().filter(is_available=True).order_by('id')
		paginator = Paginator(products, 12)
		page = request.GET.get('page')
		paged_products = paginator.get_page(page)
		product_count = products.count()

	context = {
		'products': paged_products,
		'product_count': product_count,
	}
	return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
	try:
		single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
	except Exception as e:
		raise e
	
	# Get the product gallery
	product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
	
	products = Product.objects.all().filter(is_available=True).order_by('-created_date')
	paginator = Paginator(products, 5)
	page = request.GET.get('page')
	paged_products = paginator.get_page(page)

	context = {
		'products': products,
		'products': paged_products,
		'single_product': single_product,
		'product_gallery': product_gallery,
	}
	return render(request, 'store/product.html', context)


def search(request):
	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
			product_count = products.count()
	context = {
		'products': products,
		'product_count': product_count,
	}
	return render(request, 'store/store.html', context)



class ProductCreateView(CreateView):
	model = Product
	template_name = "store/product_form.html"
	form_class = ProductForm
	permission_required = 'store.fields'
	success_url = reverse_lazy('store')

	def form_valid(self, form):
		product_form = super(ProductCreateView, self).form_valid(form)
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add New Product'
		context['submit'] = 'Create Product'
		context['head_title'] = 'Add new product'
		return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
	model = Product
	form_class = ProductForm
	success_url = reverse_lazy('product_list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Edit Product'
		context['submit'] = 'Update Product'
		context['head_title'] = 'Edit Product'
		return context

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.author:
			return True
		return False


class ProductDeleteView(DeleteView):
	model = Product
	success_url = reverse_lazy('product_list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Edit Product'
		context['submit'] = 'Delete Product'
		context['head_title'] = 'Delete Product'
		return context

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.author:
			return True
		return False