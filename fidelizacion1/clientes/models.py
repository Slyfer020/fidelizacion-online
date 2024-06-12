from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    estado = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)  
    puntos = models.IntegerField()  

    def __str__(self):
        return self.nombre_cliente

    @classmethod
    def obtener_todos(cls):
        return cls.objects.all()

        """
        En este ejemplo, se ha añadido un método llamado obtener_todos() 
        que utiliza cls.objects.all() para devolver todos los objetos de la tabla de productos. 
        Ahora, puedes llamar a este método desde cualquier parte de tu código 
        donde tengas acceso al modelo Producto. Por ejemplo:
        """
# from myapp.models import Producto  # Importa tu modelo
# Obtener todos los productos
# productos = Producto.obtener_todos()
        
# Iterar sobre los productos y hacer algo con ellos
# for producto in productos:
# print(producto.nombre, producto.descripcion, producto.precio, producto.fecha_creacion)