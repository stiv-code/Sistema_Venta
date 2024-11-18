from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.TextField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Vendedor(models.Model):
    cedula_vendedor = models.CharField(primary_key=True, max_length=10)
    nombre_vendedor = models.CharField(max_length=50)
    apellido_vendedor = models.CharField(max_length=50)
    telefono_vendedor = models.CharField(max_length=50)
    direccion = models.TextField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.cedula_vendedor
        
class Categoria(models.Model):
    id_categoria = models.CharField(primary_key=True, max_length=5)
    nombre_categoria = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.id_categoria

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=5)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre_producto = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_elaboracion = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()

    def __str__(self):
        return self.id_producto
        
class Factura(models.Model):
    id_factura = models.CharField(primary_key=True, max_length=10)
    cedula_cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    cedula_vendedor = models.ForeignKey(Vendedor, on_delete=models.RESTRICT)
    id_producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()
    iva = models.IntegerField()

    def __str__(self):
        return self.id_factura