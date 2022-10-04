
from django.db import models

# Create your models here.

class Maestro(models.Model):
    nombre_completo=models.CharField(max_length=100,default="nombre default")
    sueldo=models.DecimalField(default=1000,max_digits=8,decimal_places=2)

    def __str__(self):
        return self.nombre_completo


class Salon(models.Model):
    codigo=models.CharField(max_length=3, primary_key=True)
    letra=models.CharField(max_length=100,default="A")
    maestro=models.ForeignKey("maestro",on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo