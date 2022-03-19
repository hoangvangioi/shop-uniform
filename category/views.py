from django.shortcuts import render
from django.urls import reverse_lazy
from category.forms import CategoryForm
from .models import Category
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
# from .decorators import superuser_required
# from .forms import CommentForm, PostForm, CategoryForm


# Create your views here.


class CategoryCreateView(CreateView):
    model = Category
    template_name = "category/add_category.html"
    form_class = CategoryForm
    permission_required = 'category.fields'
    success_url = reverse_lazy('store')


    def form_valid(self, form):
        category_form = super(CategoryCreateView, self).form_valid(form)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Category'
        context['submit'] = 'Create Category'
        context['head_title'] = 'Add new category'
        return context

    # def post(self, request, *args, **kwargs):
    #     form = CategoryForm()
    #     return request()



# class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
# 	model = Category
# 	template_name = 'blog/category_form.html'
# 	form_class = CategoryForm
# 	permission_required = 'blog.fields'
# 	success_url = reverse_lazy('category_list')

# 	def form_valid(self, form):
# 		category_form = super(CategoryCreateView, self).form_valid(form)
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['title'] = 'Add New Category'
# 		context['submit'] = 'Create Category'
# 		context['head_title'] = 'Add new category'
# 		return context