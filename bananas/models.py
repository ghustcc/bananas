from django.db import models

class Lots(models.Model):
    
    nome_titular = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    hectares = models.FloatField()
    # numero = models.FloatField()

class CutOfBanana(models.Model):
    
    loteamento = models.CharField(max_length=255)
    fisrt = models.IntegerField()
    second = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    @property
    def dia_atual(self):
        return date.today().day

    @property
    def mes_atual(self):
        return date.today().month
    
    @property
    def ano_atual(self):
        return date.today().year