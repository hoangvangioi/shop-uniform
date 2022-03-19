from django.urls import path
from .views import *


urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
