from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_propriedade/', views.addPropriedade, name='addPropriedade'),
    path('propriedade/', views.propriedade, name='propriedade'),
    path('adicionar_talhao/', views.addTalhao, name='addTalhao'),
    path('adicionar_analise/', views.addAnalise, name='addAnalise'),
]