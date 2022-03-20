from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('list/', ProductListView.as_view(), name='product_list'),
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    # path('category/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', views.search, name='search'),
    # path('category/<slug:category_slug>/', ProductListView.as_view(), name='products_by_category'),
    # path('', ProductListView.as_view(), name='store'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
