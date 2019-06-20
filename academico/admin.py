from django.contrib import admin

from .models import Docente, Asignatura, Grupo

admin.site.register(Docente)
admin.site.register(Asignatura)
admin.site.register(Grupo)
