from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='pgLogin'),
    path('cadastro/', views.cadastro, name='pgCadastro'),
    path('recuperar_senha/', views.recSenha, name='recSenha'),
]