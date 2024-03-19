
from django.db import models
from molde.models import Molde,MoldeItem
from matprima.models import TipoMatPrima

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    molde = models.ForeignKey(Molde, on_delete=models.CASCADE)
    tipos_materia_prima = models.ManyToManyField(TipoMatPrima, through='Produto_TipoMatPrima', related_name='produtos')
    imagem_produto = models.ImageField(upload_to='imagens_produtos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['id']

class Produto_TipoMatPrima(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    molde_item=models.ForeignKey(MoldeItem, on_delete=models.CASCADE)
    tipo_matprima = models.ForeignKey(TipoMatPrima, on_delete=models.CASCADE)
    nome_moldeitem = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.produto.nome} - {self.tipo_matprima.nome}"
