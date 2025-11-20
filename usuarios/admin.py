from django.contrib import admin
from .models import UsuarioProdutor, UsuarioAgronomo

@admin.register(UsuarioProdutor)
class UsuarioProdutorAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'sobrenome', 'email', 'telefone')
    search_fields = ('cpf', 'nome', 'sobrenome', 'email')
    list_filter = ('data_nascimento',)


@admin.register(UsuarioAgronomo)
class UsuarioAgronomoAdmin(admin.ModelAdmin):
    list_display = ('num_crea', 'nome', 'sobrenome', 'cpf', 'email', 'telefone')
    search_fields = ('num_crea', 'nome', 'sobrenome', 'cpf', 'email')
    list_filter = ('data_nascimento',)