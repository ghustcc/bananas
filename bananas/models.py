from django.db import models

class Lots(models.Model):
    
    nome_titular = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    hectares = models.FloatField()
    numero = models.IntegerField()
    img = models.ImageField(default='img/lote.png')

class CutOfBanana(models.Model):
    
    id_lot = models.IntegerField(default=0)
    primeira = models.IntegerField()
    segunda = models.IntegerField()
    preco = models.FloatField(default=0.0)
    cotacao = models.FloatField(default=0.0)
    porcentagem = models.FloatField(default=0.0)
    kg_caixa = models.IntegerField(default=22)
    date = models.DateField()