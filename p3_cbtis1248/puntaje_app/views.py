from django.shortcuts import render

# Create your views here.

def  index(request):
    return render(request, "index.html")

def  usuarios(request):
    return render(request, "usuarios.html")

def  empleados(request):
    return render(request, "empleado.html")

def  instrumentos(request):
    return render(request, "instrumentos.html")

def  sucursales(request):
    return render(request, "sucursales.html")
