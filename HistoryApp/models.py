from django.db import models

# Create your models here.

class Temas(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()

class Admin(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    cargo = models.CharField(max_length=40)

class Membresia(models.Model):
    Nivel = models.CharField(max_length=40)
    activo = models.BooleanField()
    antiguedad = models.DateField()

