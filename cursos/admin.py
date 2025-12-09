from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'duracion_horas', 'activo', 'created')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'created'
    list_filter = ('activo',)
    readonly_fields = ('created',)

admin.site.register(Curso, CursoAdmin)
