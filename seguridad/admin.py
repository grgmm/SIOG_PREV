from django.contrib import admin
from .models import Planta, Proceso, Tag, Estandar, User

# Register your models here.
admin.site.register(Planta)
admin.site.register(Estandar)
admin.site.register(Proceso)
admin.site.register(Tag)
admin.site.register(User)


