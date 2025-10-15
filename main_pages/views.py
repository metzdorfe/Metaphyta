from django.shortcuts import render

# Create your views here.

def inicioProdutor(request):
    return render(request, 'inicioProdutor.html')

def inicioAgronomo(request):
    return render(request, 'inicioAgronomo.html')

def perfilProdutor(request):
    return render(request, 'perfilProdutor.html')

def perfilAgronomo(request):
    return render(request, 'perfilAgronomo.html')