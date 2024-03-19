from django.db import models
from produto.models import Produto
from matprima.models import MatPrima
from molde.models import MoldeItem



class ProdutoVariavel(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome_variavel = models.CharField(max_length=100)
    imagem_variavel = models.ImageField(upload_to='imagens_variavel/')
    

    def __str__(self):
        return self.nome_variavel

class ProdutoVariavelItem(models.Model):
    produto_variavel = models.ForeignKey(ProdutoVariavel, on_delete=models.CASCADE,related_name='relat_itens_produto_variavel')
    molde_item = models.ForeignKey(MoldeItem, on_delete=models.CASCADE)
    nome_item = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    matprima=models.ForeignKey(MatPrima,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome_item
    
    class Meta:
        ordering = ['id']
