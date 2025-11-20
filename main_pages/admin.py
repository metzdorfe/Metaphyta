from django.contrib import admin
from django.utils.html import format_html
from .models import FotoPerfil


@admin.register(FotoPerfil)
class FotoPerfilAdmin(admin.ModelAdmin):
    list_display = ("id", "dono", "foto_preview")
    search_fields = ("agronomo__nome", "produtor__nome")
    list_filter = ("agronomo", "produtor")

    def dono(self, obj):
        return obj.agronomo or obj.produtor

    def foto_preview(self, obj):
        if obj.foto:
            return format_html(
                "<img src='{}' width='60' style='border-radius:6px;' />",
                obj.foto.url
            )
        return "—"
    foto_preview.short_description = "Prévia"