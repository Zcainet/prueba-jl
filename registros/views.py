import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Alumnos, ComentarioContacto, Archivos
from .forms import ComentarioContactoForm, FormArchivos

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    else:
        form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})

def consultarComentarioContacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    return render(request, "registros/confirmarEliminacion.html", {'object': comentario})

def consultarComentarioIndividual(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Archivo cargado correctamente")
        else:
            messages.error(request, "Error al procesar el formulario")
    return render(request, "registros/archivos.html")

# Consultas ORM
def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2021, 7, 1)
    fechaFin = datetime.date(2021, 7, 13)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    alumnos = Alumnos.objects.filter(comentariocontacto__mensaje__contains='No Inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

# Consulta SQL cruda
def consultasSQL(request):
    alumnos = Alumnos.objects.raw(
        'SELECT id, matricula, nombre, carrera, turno, imagen '
        'FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC'
    )
    return render(request, "registros/consultas.html", {'alumnos': alumnos})
