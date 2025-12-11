from django.urls import path
from . import views

urlpatterns = [
    path('pizzas/', views.lista_pizzas, name='lista_pizzas'),
    path('pedido/nuevo/', views.crear_pedido, name='crear_pedido'),
    path('pedido/exitoso/', views.pedido_exitoso, name='pedido_exitoso'),
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
]
