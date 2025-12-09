from django.contrib import admin
from .models import Alumnos, ComentarioContacto, Archivos

class AdministrarAlumnos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

admin.site.register(Alumnos, AdministrarAlumnos)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'mensaje', 'created')
    search_fields = ('id', 'usuario', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

class ArchivosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'created')
    date_hierarchy = 'created'
    search_fields = ('titulo',)

admin.site.register(Archivos, ArchivosAdmin)
