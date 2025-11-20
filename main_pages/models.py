from django.db import models
from usuarios.models import UsuarioAgronomo, UsuarioProdutor


class FotoPerfil(models.Model):
    agronomo = models.OneToOneField(
        UsuarioAgronomo,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    produtor = models.OneToOneField(
        UsuarioProdutor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    foto = models.ImageField(
        upload_to="fotos_perfil/",
        default="fotos_perfil/not_user.jpg"
    )

    def __str__(self):
        dono = self.agronomo or self.produtor
        return f"Foto de {dono}"