from django.db import models

# Create your models here.


class Gdp(models.Model):
    
    name = models.CharField(max_length=30)
  

    
    def __str__(self):
    
        return self.name

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
  

    
    def __str__(self):
    
       return '%s, %s' % (self.apellido, self.nombre)


class Planta(models.Model):
    
    nombre = models.CharField(max_length=30)
    id_estandar = models.CharField(max_length=30)
  

    
    def __str__(self):
    
       return '%s' % (self.nombre,)


class Estandar(models.Model):
    
    nombre = models.CharField(max_length=30)
    id_procesos = models.CharField(max_length=30)
  

    
    def __str__(self):
    
       return '%s' % (self.nombre,)


class Proceso(models.Model):
    
    nombre = models.CharField(max_length=30)
    id_estandar = models.CharField(max_length=30)
  

    
    def __str__(self):
    
       return '%s' % (self.nombre,)

class Tag(models.Model):
    
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    id_planta= models.CharField(max_length=30)
    
      
    def __str__(self):
    
       return '%s' % (self.nombre,)

