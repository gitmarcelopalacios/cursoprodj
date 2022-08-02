from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombres = models.CharField('Nombres y Apellidos', max_length=120)
    dni = models.CharField('Número de DNI',max_length=8)
    telefono = models.CharField('Teléfono', max_length=100)
    correo_electronico = models.CharField('Email', max_length=200)
    curso = models.CharField('Curso', max_length=10)