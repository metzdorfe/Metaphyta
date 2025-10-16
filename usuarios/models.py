from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UsuarioProdutor(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    class Meta:
        db_table = 'usuario_produtor'

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    # Criptografa a senha antes de salvar
    def set_senha(self, senha_plana):
        self.senha = make_password(senha_plana)

    # Verifica se a senha está correta
    def verificar_senha(self, senha_plana):
        return check_password(senha_plana, self.senha)


class UsuarioAgronomo(models.Model):
    num_crea = models.CharField(primary_key=True, max_length=20)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    class Meta:
        db_table = 'usuario_agronomo'

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    def set_senha(self, senha_plana):
        self.senha = make_password(senha_plana)

    def verificar_senha(self, senha_plana):
        return check_password(senha_plana, self.senha)