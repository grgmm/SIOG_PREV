from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _ 
from .managers import UserManager

# Create your models here.

#class Car(models.Model):
 #   manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
 
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
 
    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
 
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)




class Proceso(models.Model):
    
    nombre = models.CharField(max_length=30)
   # estandar = models.ManyToManyField(Estandar)#

    
    def __str__(self):
    
       return '%s' % (self.nombre,)


class Estandar(models.Model):
    
    nombre = models.CharField(max_length=30)
    idproceso = models.ManyToManyField(Proceso)
  

    
    def __str__(self):
    
       return '%s' % (self.nombre,)


class Planta(models.Model):
    
    nombre = models.CharField(max_length=30)
    id_estandar = models.ForeignKey(Estandar, on_delete=models.CASCADE)

    
    def __str__(self):
    
       return '%s' % (self.nombre,)



class Tag(models.Model):
    
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    id_planta= models.ForeignKey(Planta, on_delete=models.CASCADE)
    
      
    def __str__(self):
    
       return '%s' % (self.nombre,)

