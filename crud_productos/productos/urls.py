from django.conf.urls import url
from productos import views

urlpatterns = [
    url(r'^crear$', views.CreateProductView.as_view(), name='crear'),
    url(r'^actualizar/(?P<pk>\d+)$', views.UpdateProductView.as_view(), name='actualizar'),
    url(r'^eliminar/(?P<pk>\d+)$', views.DeleteProductView.as_view(), name='eliminar'),
    url(r'^$', views.ProductsView.as_view(), name='productos'),
]
