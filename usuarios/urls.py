from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='pgLogin.html'),
    path('cadastro/', views.cadastro, name='pgCadastro.html'),
    path('recuperar_senha/', views.recSenha, name='recuperar_senha'),

]