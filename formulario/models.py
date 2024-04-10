from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
