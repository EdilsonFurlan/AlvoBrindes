from django.db import models
from django.utils import timezone

class SubTipoMatPrima(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class TipoMatPrima(models.Model):
    UNIDADE_CHOICES = [
        ('M', 'Metro'),
        ('P', 'Peça'),
    ]
    
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=1, choices=UNIDADE_CHOICES)
    largura = models.IntegerField(null=True, blank=True)
    data_atualizacao_preco = models.DateField(default=timezone.now)
    subtipo_matprima = models.ForeignKey(SubTipoMatPrima, on_delete=models.CASCADE, related_name='subtipos')

    def __str__(self):
        return self.nome

class MatPrima(models.Model):
    nome = models.CharField(max_length=50)
    tipo_matprima = models.ForeignKey(TipoMatPrima, on_delete=models.CASCADE, related_name='tipo_matprimas')

    def __str__(self):
        return self.nome

