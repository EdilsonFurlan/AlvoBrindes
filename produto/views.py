from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from molde.models import Molde,MoldeItem
from matprima.models import TipoMatPrima
from .models import Produto,Produto_TipoMatPrima
from django.contrib import messages
from django.contrib.messages import constants

def adicionar_produto(request):

    moldes = Molde.objects.all()
       
    
    return render(request,'add_produto.html',{'moldes':moldes})



def salvar_produto(request):
    if request.method == 'POST':
        # Criando uma instância de Produto
        produto = Produto(nome=request.POST['nome'], molde_id=request.POST.get('molde'))
        print (produto.nome)

        # Salvando a imagem do produto
        if 'imagem_produto' in request.FILES:
            produto.imagem_produto = request.FILES['imagem_produto']

        # Salvando o Produto no banco de dados para obter um ID
        print('Salvando PRODUTOS')
        produto.save()

        # Iterando sobre os campos do formulário que representam os itens de Produto_TipoMatPrima
        for i in range(0, len(request.POST.getlist('idTipoMatPrima[]'))):
            print('FOR I')
            # Criando uma instância de Produto_TipoMatPrima
            item_produto = Produto_TipoMatPrima(
                produto=produto,
                tipo_matprima_id=request.POST.getlist('idTipoMatPrima[]')[i],
                molde_item_id=request.POST.getlist('idMoldeItem[]')[i],
                nome_moldeitem=request.POST.getlist('nomeMoldeItem[]')[i],
                quantidade=request.POST.getlist('quantidade[]')[i],
            )
            # Salvando o item de Produto_TipoMatPrima no banco de dados
            print('Salvando Itenssssss')
            item_produto.save()

        # Redirecionando para uma página de sucesso após salvar tudo
        messages.add_message(request, constants.SUCCESS, 'Produto Cadastrado com Sucesso!.')
        return redirect('/produto/adicionar_produto/')

    else:
        # Se não for uma solicitação POST, renderize o formulário para criar um novo Produto
        return render(request, 'adicionar_produto.html')


def buscar_molde_itens(request, id_molde):
    
    # Filtrando os MoldeItens com base no ID do molde fornecido
    molde_itens = MoldeItem.objects.filter(molde_id=id_molde)

    # Criando uma lista para armazenar os dados dos MoldeItens
    molde_itens_data = []

    # Iterando sobre os objetos MoldeItem e adicionando seus dados à lista
    for molde_item in molde_itens:
        
        molde_itens_data.append({
            'id': molde_item.id,
            'nome': molde_item.nome,
            'quantidade': molde_item.quantidade,
            'id_subtipo' : molde_item.subtipo_matprima_id,
            'subtipo_nome' : molde_item.subtipo_matprima.nome,
            
            # Adicione outros campos conforme necessário
            
        })

    # Retornando os dados em formato JSON
    return JsonResponse({'molde_itens': molde_itens_data})

def buscar_matprima_tipo(request, id_tipo):
    
    # Filtrando os tipos de matéria-prima com base no ID do subtipo fornecido
   
    tipos_matprima = TipoMatPrima.objects.filter(subtipo_matprima_id=id_tipo)

    # Criando uma lista para armazenar os dados dos tipos de matéria-prima
    tipos_matprima_data = []

    # Iterando sobre os objetos TipoMatPrima e adicionando seus dados à lista
    for tipo_matprima in tipos_matprima:
        print(tipo_matprima.id)
        tipos_matprima_data.append({
            'id': tipo_matprima.id,
            'nome': tipo_matprima.nome,
            # Adicione outros campos conforme necessário
        })

    # Retornando os dados em formato JSON
    return JsonResponse({'tipos_matprima': tipos_matprima_data})



