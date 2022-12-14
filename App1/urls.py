from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('lacteos/', iniciolacteos, name='iniciolacteos'),
    path('galletitas/', iniciogalletitas, name='iniciogalletitas'),
    path('bebidas/', iniciobebidas, name='iniciobebidas'),
    path('formularioProducto/', formularioProducto, name='formularioProducto'),
    path('formularioProductoApi/', formularioProductoApi, name='formularioProductoApi'),
    path('busquedaProducto/', busquedaProducto, name='busquedaProducto'),
    path('buscar/', buscar, name='buscar'),
]