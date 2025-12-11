# Register your models here.
from django.contrib import admin
from .models import Pizza, Pedido, PedidoPizza

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "disponible")
    list_filter = ("disponible",)
    search_fields = ("nombre",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_cliente", "estado", "fecha")
    list_filter = ("estado", "fecha")
    search_fields = ("nombre_cliente", "direccion", "telefono")
    date_hierarchy = "fecha"


@admin.register(PedidoPizza)
class PedidoPizzaAdmin(admin.ModelAdmin):
    list_display = ("pedido", "pizza", "cantidad")
