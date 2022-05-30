from django.db import models

class familiares(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()

