from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from produto.models import Produto,Produto_TipoMatPrima
from matprima.models import MatPrima
from django.contrib import messages
from django.contrib.messages import constants
from django.db import transaction
from .models import ProdutoVariavel, ProdutoVariavelItem

def add_produto_variavel(request):

    produto= Produto.objects.all()

    return render(request,'add_produto_variavel.html',{'produtos':produto})

def buscar_produto_itens(request, produto_id):
    # Filtra os objetos Produto_TipoMatPrima relacionados ao produto específico
    prod_itens = Produto_TipoMatPrima.objects.filter(produto_id=produto_id)
    
    # Criando uma lista para armazenar os dados dos tipos de matéria-prima
    itens_data = []

    # Iterando sobre os objetos Produto_TipoMatPrima e adicionando seus dados à lista
    for item in prod_itens:
        itens_data.append({
            'id': item.id,
            'nome_moldeitem': item.nome_moldeitem,
            'quantidade': item.quantidade,
            'tipo_matprima': item.tipo_matprima_id,
            'molde_item_id': item.molde_item_id,
            # Adicione outros campos conforme necessário
        })

    return JsonResponse({'prod_itens': itens_data})


def buscar_matprima(request,tipo_id):
   
    #Filtra MatPrima por TipoMatPrima
    matprima = MatPrima.objects.filter(tipo_matprima_id=tipo_id)

        # Criando uma lista para armazenar os dados dos tipos de matéria-prima
    itens_data = []

    # Iterando sobre os objetos Produto_TipoMatPrima e adicionando seus dados à lista
    for item in matprima:

        
        itens_data.append({
            'id': item.id,
            'nome_matprima': item.nome,
            
            # Adicione outros campos conforme necessário
        })

    return JsonResponse({'matprimas': itens_data})



#**************Salvar Produto Variavel*********************

def salvar_produto_variavel(request):
    
    try:
        
          # Verifica se a solicitação é um POST
        if request.method == 'POST':
            # Obtém os dados do formulário
            nome_variavel = request.POST.get('nome_variavel')
            cmbproduto=request.POST.get('cmbproduto')

            # Salvando a imagem do produto
            if 'imagem_variavel' in request.FILES:
            
                print('entrou no if')
               
                imagem_variavel = request.FILES['imagem_variavel']
                print(imagem_variavel)
            else:
                print('Entrou no Else')
                imagem_variavel = None 
            
            # Verificação de campos obrigatórios
            if not (nome_variavel and cmbproduto):
                raise ValueError("Todos os campos devem ser preenchidos")
                        
            #Matrizes dos itens do Produto_Variavel
            molde_item = request.POST.getlist('molde_item[]')
            nome_item = request.POST.getlist('nome_item[]')
            quantidade = request.POST.getlist('quantidade[]')
            matprima= request.POST.getlist('matprima[]')
        
           # Validação de entrada - certifique-se de que as listas de itens tenham o mesmo comprimento
            if not all(len(lst) == len(molde_item) for lst in [nome_item, quantidade, matprima]):
                raise ValueError("Listas de itens inconsistentes")
            
            # Salvar o ProdutoVariavel dentro de uma transação atômica
            with transaction.atomic():
                produto_variavel = ProdutoVariavel.objects.create(
                nome_variavel=nome_variavel,
                produto_id=cmbproduto,
                imagem_variavel=imagem_variavel
                )

                # Salvar os itens do ProdutoVariavel
                for molde_id, nome, qtd, matprima_id in zip(molde_item, nome_item, quantidade, matprima):
                    ProdutoVariavelItem.objects.create(
                        produto_variavel=produto_variavel,
                        molde_item_id=molde_id,
                        nome_item=nome,
                        quantidade=qtd,
                        matprima_id=matprima_id
                    )

            messages.add_message(request, constants.SUCCESS, 'Produto Variavel salvo com sucesso')
            return redirect('/produto_variavel/add_produto_variavel/')

    except Exception as e:
        # Lidar com exceções
        messages.add_message(request, constants.ERROR, f'Erro ao salvar Produto Variavel: {e}')
        return redirect('/produto_variavel/add_produto_variavel/')
    
#**************Fim Salvar Produto Variavel*********************

