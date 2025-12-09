from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del curso")
    descripcion = models.TextField(verbose_name="Descripción")
    duracion_horas = models.IntegerField(verbose_name="Duración (horas)")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    imagen = models.ImageField(upload_to='cursos', null=True, blank=True, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre
