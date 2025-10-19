from django.urls import path
from . import views

urlpatterns = [
    # Páginas iniciais protegidas
    path('pagina_inicial_produtor/', views.inicioProdutor, name='inicioProdutor'),
    path('pagina_inicial_agronomo/', views.inicioAgronomo, name='inicioAgronomo'),
    
    # Páginas de perfil protegidas
    path('perfil_produtor/', views.perfilProdutor, name='perfilProdutor'),
    path('perfil_agronomo/', views.perfilAgronomo, name='perfilAgronomo'),

    # Novos endpoints de login/logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Redirecionamento inicial
    path('', views.home_redirect, name='home_redirect'),
]
