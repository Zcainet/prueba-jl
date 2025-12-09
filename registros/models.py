from django.db import models

class Alumnos(models.Model):
    matricula = models.CharField(max_length=12, verbose_name="Matrícula")
    nombre = models.TextField(verbose_name="Nombre")
    carrera = models.TextField(verbose_name="Carrera")
    turno = models.CharField(max_length=10, verbose_name="Turno")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
    #Indica que se mostrára el nombre como valor en la tabla

class ComentarioContacto(models.Model):
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario de Contacto"
        verbose_name_plural = "Comentarios de Contacto"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje

class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo
