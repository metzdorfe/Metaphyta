from django.contrib import admin
from .models import UsuarioAgronomo, UsuarioProdutor

def auto_list_display(model):
    return [field.name for field in model._meta.fields]

@admin.register(UsuarioAgronomo)
class UsuarioAgronomoAdmin(admin.ModelAdmin):
    list_display = auto_list_display(UsuarioAgronomo)
    search_fields = ["nome", "sobrenome", "cpf", "email"]


@admin.register(UsuarioProdutor)
class UsuarioProdutorAdmin(admin.ModelAdmin):
    list_display = auto_list_display(UsuarioProdutor)
    search_fields = ["nome", "sobrenome", "cpf", "email"]
    list_filter = ["agronomo_relacionado"]
