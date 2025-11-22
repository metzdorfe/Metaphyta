from django.contrib import admin
from .models import (Propriedade, Talhao, Analise, AnaliseTalhao, AnalisesPropriedade)

# Função para auto-exibir todos os campos
def auto_list_display(model):
    return [field.name for field in model._meta.fields]


@admin.register(Propriedade)
class PropriedadeAdmin(admin.ModelAdmin):
    list_display = auto_list_display(Propriedade)
    search_fields = ["nome_propriedade", "codigo_propriedade"]
    list_filter = ["uf"]


@admin.register(Talhao)
class TalhaoAdmin(admin.ModelAdmin):
    list_display = auto_list_display(Talhao)
    search_fields = ["codigo_talhao", "cultura"]
    list_filter = ["cultura"]


@admin.register(Analise)
class AnaliseAdmin(admin.ModelAdmin):
    list_display = auto_list_display(Analise)


@admin.register(AnaliseTalhao)
class AnaliseTalhaoAdmin(admin.ModelAdmin):
    list_display = auto_list_display(AnaliseTalhao)


@admin.register(AnalisesPropriedade)
class AnalisesPropriedadeAdmin(admin.ModelAdmin):
    list_display = auto_list_display(AnalisesPropriedade)
