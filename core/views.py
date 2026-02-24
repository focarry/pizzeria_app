from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Pizza, Pedido, PedidoPizza

def lista_pizzas(request):
    pizzas = Pizza.objects.filter(disponible=True)
    return render(request, "core/lista_pizzas.html", {"pizzas": pizzas})


def crear_pedido(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre_cliente")
        direccion = request.POST.get("direccion")
        telefono = request.POST.get("telefono")

        # Crear el pedido
        pedido = Pedido.objects.create(
            nombre_cliente=nombre,
            direccion=direccion,
            telefono=telefono
        )

        # Agregar pizzas con cantidades
        for key, value in request.POST.items():
            if key.startswith("pizza_"):
                pizza_id = key.split("_")[1]
                cantidad = int(value)
                if cantidad > 0:
                    pizza = Pizza.objects.get(id=pizza_id)
                    PedidoPizza.objects.create(
                        pedido=pedido,
                        pizza=pizza,
                        cantidad=cantidad
                    )

        return redirect("pedido_exitoso")

    pizzas = Pizza.objects.filter(disponible=True)
    return render(request, "core/crear_pedido.html", {"pizzas": pizzas})


def pedido_exitoso(request):
    return render(request, "core/pedido_exitoso.html")

def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha')  # últimos primero
    return render(request, 'core/listar_pedidos.html', {'pedidos': pedidos})
