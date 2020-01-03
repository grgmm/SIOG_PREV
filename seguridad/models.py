from django.db import models

# Create your models here.

#class Car(models.Model):
 #   manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Gdp(models.Model):
    
    name = models.CharField(max_length=30)
  

    
    def __str__(self):
    
        return self.name




class Estandar(models.Model):
    
    nombre = models.CharField(max_length=30)
  

    
    def __str__(self):
    
       return '%s' % (self.nombre,)


class Planta(models.Model):
    
    nombre = models.CharField(max_length=30)
    id_estandar = models.ForeignKey(Estandar, on_delete=models.CASCADE)

    
    def __str__(self):
    
       return '%s' % (self.nombre,)


class Proceso(models.Model):
    
    nombre = models.CharField(max_length=30)
  

    
    def __str__(self):
    
       return '%s' % (self.nombre,)

class Tag(models.Model):
    
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    id_planta= models.ForeignKey(Planta, on_delete=models.CASCADE)
    
      
    def __str__(self):
    
       return '%s' % (self.nombre,)

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    id_planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    id_gdp = models.ForeignKey(Gdp, on_delete=models.CASCADE)

  

    
    def __str__(self):
    
       return '%s, %s' % (self.apellido, self.nombre)
