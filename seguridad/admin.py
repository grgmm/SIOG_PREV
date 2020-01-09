from django.contrib import admin
from .models import Planta, Proceso, Tag, Estandar

# Register your models here.
admin.site.register(Planta)
admin.site.register(Estandar)
admin.site.register(Proceso)
admin.site.register(Tag)


