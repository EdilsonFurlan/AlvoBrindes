from django.db import models
from matprima.models import SubTipoMatPrima

class Molde(models.Model):
    nome_molde = models.CharField(max_length=50)
    imagem_molde=models.ImageField(upload_to='imagens_moldes/',blank=True,null=True)

    def __str__(self):
        return self.nome_molde
    

class MoldeItem(models.Model):
    molde = models.ForeignKey(Molde, related_name='itens', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    quantidade_x =models.IntegerField(default=1)
    altura = models.IntegerField(default=0,null=True,blank=True)
    largura = models.IntegerField(default=0,null=True,blank=True)
    subtipo_matprima = models.ForeignKey(SubTipoMatPrima,on_delete=models.CASCADE)
    quantidade=models.IntegerField()

    def __str__(self):
        return self.nome
