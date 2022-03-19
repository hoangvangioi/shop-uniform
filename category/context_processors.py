from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


from django.db.models import Count

def get_category_count():
	category_query = Category.objects.values('categories__slug', 'categories__title').annotate(Count('categories__title'))
	return category_query

def sidebar(request):
	category_count = get_category_count()
	most_recent = Category.objects.order_by('-timestamp')[:3]
	context = {
		'most_recent': most_recent,
		'category_count': category_count,
	}
	return context