from django.shortcuts import render

def formulario(request):
    return render(request, "inicio/formulario.html")
