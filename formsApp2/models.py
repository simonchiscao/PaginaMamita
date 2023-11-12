from django.db import models

# Create your models here.
class Preguntas(models.Model):
    nombre = models.CharField(max_length=14)
    email= models.CharField(max_length=40)
    edad = models.IntegerField()
    respuestaOne = models.CharField(max_length=200)

    


