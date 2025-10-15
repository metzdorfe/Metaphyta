from django.urls import path
from . import views

urlpatterns = [
    path('pagina_inicial_produtor/', views.inicioProdutor, name='inicioProdutor.html'),
    path('pagina_inicial_agronomo/', views.inicioAgronomo, name='inicioAgronomo.html'),
    path('perfil_produtor/', views.perfilProdutor, name='perfilProdutor.html'),
    path('perfil_agronomo/', views.perfilAgronomo, name='perfilAgronomo.html')
]