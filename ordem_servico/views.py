from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.db import transaction
from produto_variavel.models import ProdutoVariavel
from .models import OrdemServico, OrdemServicoItem


def add_ordem_servico(request):

    variavel=ProdutoVariavel.objects.all()
    
    return render(request, 'add_ordem_servico.html',{'variaveis':variavel})



def adicionar_combobox(request):
    
   
    produtos_variaveis = ProdutoVariavel.objects.all()
    
    # Criando uma lista para armazenar os dados dos produtos variáveis
    data = []

    # Iterando sobre os objetos ProdutoVariavel e adicionando seus dados à lista
    for item in produtos_variaveis:
        data.append({
            'id': item.id,
            'nome_variavel': item.nome_variavel,
            'imagem_variavel': item.imagem_variavel.url,  # Use .url para obter a URL da imagem
            # Adicione outros campos conforme necessário
   
        })
    
    return JsonResponse({'produtosVariaveis': data})




def salvar_ordem_servico(request):
    try:

        if request.method == 'POST':
        
            
                descricao = request.POST.get('descricao')
                
                  # Verificação de campos obrigatórios
                if not (descricao):
                    raise ValueError("Todos os campos da Ordem devem ser preenchidos")
                
                
                #Matrizes dos itens do Produto_Variavel
                produto_variavels_id = request.POST.getlist('produto_variavel[]')
                quantidades = request.POST.getlist('quantidade[]')

                 # Validação de entrada - certifique-se de que existem itens
                if not (produto_variavels_id and quantidades):
                    raise ValueError("Pelo menos um item de Produto Variável e quantidade devem ser fornecidos")
            
                
            # Validação de entrada - certifique-se de que as listas de itens tenham o mesmo comprimento
                if not all(len(lst) == len(produto_variavels_id) for lst in [quantidades]):
                    raise ValueError("Listas de itens inconsistentes")


        with transaction.atomic():
                
                
                
                #Salva Ordem de Serviço e retorna o objeto OrdemServico criado
                ordem_servico = OrdemServico.objects.create(descricao=descricao)

                produto_variavels_id = request.POST.getlist('produto_variavel[]')
                quantidades = request.POST.getlist('quantidade[]')

                for produto_variavel_id, quantidade in zip(produto_variavels_id, quantidades):
                    produto_variavel = ProdutoVariavel.objects.get(pk=produto_variavel_id)
                    #Salva Ordem de Serviço Item 
                    OrdemServicoItem.objects.create(ordem_servico=ordem_servico, produto_variavel=produto_variavel, quantidade=quantidade)

        messages.add_message(request, constants.SUCCESS, 'Produto Variavel salvo com sucesso')
        return redirect('/ordem_servico/add_ordem_servico/')

    except Exception as e:
        # Lidar com exceções
        messages.add_message(request, constants.ERROR, f'Erro ao salvar Produto Variavel: {e}')
        return redirect('/ordem_servico/add_ordem_servico/')
#**************Fim Salvar Produto Variavel*********************

#**************Calcula Total*********************

from django.db.models import F, ExpressionWrapper, IntegerField
from produto_variavel.models import ProdutoVariavelItem

from django.db.models import Count,Sum


def calcula_total1(request):
         
    # Filtrar objetos OrdemServico com status "Aberto"
    ordens_abertas = OrdemServico.objects.filter(status="Aberto")

    # Filtrar OrdemServicoItem associados a ordens abertas e agrupar por produto_variavel
    soma_quantidades_produto_variavel = OrdemServicoItem.objects.filter(ordem_servico__in=ordens_abertas).values('produto_variavel', 'produto_variavel__nome_variavel').annotate(soma_quantidades=Sum('quantidade'))

    # Agora você pode iterar sobre os resultados e acessar o ID, nome_variavel e soma das quantidades para cada produto_variavel
    for soma_produto_variavel in soma_quantidades_produto_variavel:
        produto_variavel_id = soma_produto_variavel['produto_variavel']
        nome_variavel = soma_produto_variavel['produto_variavel__nome_variavel']
        soma_quantidades = soma_produto_variavel['soma_quantidades']
        print(f"Produto Variável ID: {produto_variavel_id}, Nome: {nome_variavel}, Soma das Quantidades: {soma_quantidades}")

    return JsonResponse({'success': True})

def calcula_total2(request):
        # Filtrar objetos OrdemServico com status "Aberto"
    ordens_abertas = OrdemServico.objects.filter(status="Aberto")

    # Filtrar OrdemServicoItem associados a ordens abertas e agrupar por produto_variavel
    soma_quantidades_produto_variavel = OrdemServicoItem.objects.filter(ordem_servico__in=ordens_abertas).values('produto_variavel', 'produto_variavel__nome_variavel').annotate(soma_quantidades=Sum('quantidade')).prefetch_related('produto_variavel__relat_itens_produto_variavel')

    # Agora você pode iterar sobre os resultados e acessar os itens relacionados para cada produto_variavel
    for soma_produto_variavel in soma_quantidades_produto_variavel:
        produto_variavel_id = soma_produto_variavel['produto_variavel']
        nome_variavel = soma_produto_variavel['produto_variavel__nome_variavel']
        soma_quantidades = soma_produto_variavel['soma_quantidades']
        
        print(f"Produto Variável ID: {produto_variavel_id}, Nome: {nome_variavel}, Soma das Quantidades: {soma_quantidades}")
        
        # Acessando os itens relacionados de ProdutoVariavelItem
        itens_produto_variavel = soma_produto_variavel['produto_variavel__relat_itens_produto_variavel_id']
        for item in itens_produto_variavel:
            print(f"  - Produto Variável Item: {item}")
    return JsonResponse({'SUCCESS':True})

def calcula_total3(request):
        # Obtendo todos os ProdutoVariavel
    produtos_variaveis = ProdutoVariavel.objects.all()

    # Iterando sobre cada ProdutoVariavel
    for produto_variavel in produtos_variaveis:
        print(f"Produto Variável: {produto_variavel.id} - {produto_variavel.nome_variavel}")
        
        # Obtendo os itens do ProdutoVariavel
        itens_produto_variavel = ProdutoVariavelItem.objects.filter(produto_variavel=produto_variavel)
        
        # Iterando sobre cada item do ProdutoVariavel
        for item in itens_produto_variavel:
            print(f" - Nome do Item: {item.nome_item} - Qtd {item.quantidade}")
            
            # Adicione mais informações aqui, se necessário
        print("\n")  # Adicionando uma linha em branco entre os produtos variáveis
    return JsonResponse({'SUCCESS':True})

from django.db.models import F, Sum




def calcula_total4(request):
    ordem=OrdemServicoItem.objects.all()
    for p in ordem:
        print(f"{p.produto_variavel_id} - {p.produto_variavel} - {p.quantidade}")
      
       
       
    return JsonResponse({'SUCCESS':True})

from matprima.models import MatPrima
from django.db.models import F
def calcula_total(request):

        # Buscar todos os objetos OrdemServicoItem
    ordens_servico = OrdemServicoItem.objects.all()

    # Iterar sobre os objetos OrdemServicoItem
    for ordem_servico_item in ordens_servico:
        print(f"Ordem de Serviço: {ordem_servico_item.ordem_servico}")
        print(f"  - Produto Variável: {ordem_servico_item.produto_variavel}")
        print(f"  - Quantidade: {ordem_servico_item.quantidade}")

        # Filtrar os itens de ProdutoVariavelItem relacionados a este OrdemServicoItem
        itens_produto_variavel = ProdutoVariavelItem.objects.filter(produto_variavel=ordem_servico_item.produto_variavel)

        # Agrupar por MatPrima e calcular a soma da quantidade
        soma_por_matprima = itens_produto_variavel.values('matprima').annotate(total_quantidade=Sum('quantidade'))

        # Iterar sobre os resultados da soma por MatPrima e imprimir
        for soma in soma_por_matprima:
            matprima = MatPrima.objects.get(pk=soma['matprima'])
            quantidade_total = soma['total_quantidade'] * ordem_servico_item.quantidade
            print(f"     - Matéria-Prima: {matprima.nome}, Quantidade Total: {quantidade_total}")
    
    return JsonResponse({'SUCCESS':True})