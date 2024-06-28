from django.db import models

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