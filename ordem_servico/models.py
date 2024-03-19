from django.db import models
from produto_variavel.models import ProdutoVariavel

class OrdemServico(models.Model):
    data_abertura = models.DateField(auto_now_add=True)
    data_fechamento = models.DateField(auto_now=True)
    descricao = models.CharField(max_length=100)
    status = models.CharField(max_length=20,default='Aberto')
    
    def __str__(self):
        return self.descricao

class OrdemServicoItem(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    produto_variavel = models.ForeignKey(ProdutoVariavel, on_delete=models.CASCADE,related_name='relat_itens_servico')
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ordem_servico.descricao} - {self.produto_variavel.nome_variavel}"
    
    class Meta:
        ordering = ['id']