from django.db import models

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('preparando', 'Preparando'),
        ('en_camino', 'En camino'),
        ('entregado', 'Entregado'),
    ]

    nombre_cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente'
    )

    pizzas = models.ManyToManyField("Pizza", through="PedidoPizza")

    def __str__(self):
        return f"Pedido #{self.id} - {self.nombre_cliente}"


class PedidoPizza(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}x {self.pizza.nombre} en Pedido {self.pedido.id}"
