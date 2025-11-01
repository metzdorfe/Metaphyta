from django.urls import path
from . import views

urlpatterns = [
    path('pagina_inicial_produtor/', views.pagina_inicial_produtor, name='pagina_inicial_produtor'),
    path('pagina_inicial_agronomo/', views.pagina_inicial_agronomo, name='pagina_inicial_agronomo'),
    #path('perfil_produtor/', views.perfilProdutor, name='perfilProdutor'),
    #path('perfil_agronomo/', views.perfilAgronomo, name='perfilAgronomo'),
    #path('login/', views.login_view, name='login'),
    #path('logout/', views.logout_view, name='logout'),
    #path('', views.home_redirect, name='home_redirect'),
]