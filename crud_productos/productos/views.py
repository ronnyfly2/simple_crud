from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Product
from .forms import ProductForm

# Create your views here.

class ProductsView(ListView):
    model = Product
    template_name = 'index.html'


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'form.html'
    success_url = reverse_lazy('productos')

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Producto'
        return context


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'form.html'
    form_class = ProductForm
    success_url = reverse_lazy('productos')

    def get_context_data(self, **kwargs):
        context = super(UpdateProductView, self).get_context_data(**kwargs)
        context['title'] = 'Actualizar producto'
        return context


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('productos')
