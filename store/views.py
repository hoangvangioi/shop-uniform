from django.shortcuts import render, get_object_or_404
from .models import Product, ProductGallery#, Profile
from category.models import Category
from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


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
    
    # userprofile = get_object_or_404(Profile, user=request.user)
    
    context = {
        'products': products,
        'products': paged_products,
        'single_product': single_product,
        'product_gallery': product_gallery,
        
        # 'userprofile': userprofile,
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
