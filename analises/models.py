from django.db import models
from usuarios.models import UsuarioAgronomo, UsuarioProdutor

#Create your models here

#Propriedade
class Propriedade(models.Model):
    codigo_propriedade = models.CharField(primary_key=True, max_length=13)
    nome_propriedade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=255)

    produtor = models.ForeignKey(
        UsuarioProdutor,
        on_delete=models.CASCADE,
        related_name="propriedades"
    )

    class Meta:
        db_table = "propriedade"
        
    def __str__(self):
        return self.nome_propriedade

#Talhão
class Talhao(models.Model):
    codigo_talhao = models.CharField(primary_key=True, max_length=100)

    codigo_propriedade = models.ForeignKey(
        Propriedade,
        on_delete=models.CASCADE,
        related_name='talhoes'
    )

    cultura = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_solo = models.CharField(max_length=100)
    observacao = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'talhao'

    def __str__(self):
        return f"{self.codigo_talhao} - {self.cultura}"

#dados da analise
class Analise(models.Model):
    codigo_analise = models.CharField(primary_key=True, max_length=12)
    nome_analise = models.CharField(max_length=150)
    tipo_analise = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_analise

#analise quimica do talhão
class AnaliseTalhao(models.Model):
    id_analise = models.AutoField(primary_key=True)

    codigo_talhao = models.ForeignKey(
        Talhao,
        on_delete=models.CASCADE,
        related_name='analises'
    )

    laboratorio_responsavel = models.CharField(max_length=100, null=True, blank=True)

    ph = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    mo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    ctc = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    acidez = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    calcio = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    magnesio = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    potassio = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fosforo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    enxofre = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    ferro = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    manganes = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    zinco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    cobre = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    boro = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    aluminio = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'analise_talhao'

    def __str__(self):
        return f"Análise {self.id_analise} - Talhão {self.codigo_talhao_id}"


class AnalisesPropriedade(models.Model):
    id = models.AutoField(primary_key=True)

    codigo_propriedade = models.ForeignKey(
        Propriedade,
        on_delete=models.CASCADE,
        related_name='analises'
    )

    codigo_analise = models.ForeignKey(
        Analise,
        on_delete=models.CASCADE,
        related_name='propriedades'
    )

    data_realizacao = models.DateField()
    resultado = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigo_propriedade} - {self.codigo_analise}"