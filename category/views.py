from django.urls import reverse_lazy
from category.forms import CategoryForm
from .models import Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView


# Create your views here.


class CategoryListView(ListView):
	model = Category
	template_name = 'category/category_list_form.html'
	context_object_name = 'category'
	ordering = ['-id']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Lists of Category'
		context['head_title'] = 'Lists of Category'
		return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = "category/category_form.html"
    form_class = CategoryForm
    permission_required = 'category.fields'
    success_url = reverse_lazy('category_list')


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


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
	model = Category
	form_class = CategoryForm
	success_url = reverse_lazy('category_list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Edit Category'
		context['submit'] = 'Update Category'
		context['head_title'] = 'Edit Category'
		return context

	def test_func(self):
		category = self.get_object()
		if self.request.user == category.author:
			return True
		return False


class CategoryDeleteView(DeleteView):
	model = Category
	success_url = reverse_lazy('category_list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Edit Category'
		context['submit'] = 'Delete Category'
		context['head_title'] = 'Delete Category'
		return context

	def test_func(self):
		category = self.get_object()
		if self.request.user == category.author:
			return True
		return False