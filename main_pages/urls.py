from django.urls import path
from . import views

urlpatterns = [
    path('pagina_inicial_agronomo/', views.pagina_inicial_agronomo, name='paginaInicialAgronomo'),
    path('pagina_inicial_produtor/', views.pagina_inicial_produtor, name='paginaInicialProdutor'),
    path('perfil_agronomo/', views.perfilAgronomo, name='perfilAgronomo'),
    path('perfil_produtor/', views.perfilProdutor, name='perfilProdutor')
]
