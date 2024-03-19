from django.shortcuts import render,redirect
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages import constants
from django.http import HttpResponse,JsonResponse
from produto.models import Produto
from matprima.models import SubTipoMatPrima
from .models import Molde,MoldeItem

def add_molde(request):
    produtos = Produto.objects.all()

    moldes=Molde.objects.all()
    
    return render(request, 'add_molde.html', {'produtos': produtos, 'moldes': moldes})


# Salva o Molde e  Itens do Molde
def salvar_molde(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Salvar o molde
                nome_molde = request.POST.get('nome_molde')
                print(nome_molde)
                imagem = None
                if 'imagem_molde' in request.FILES:
                    imagem = request.FILES.get('imagem_molde')
                molde = Molde(nome_molde=nome_molde, imagem_molde=imagem)
                molde.save()

                # Salvar os itens do molde
                nomes_itens = request.POST.getlist('nome')
                quantidades_x = request.POST.getlist('quantidade_x')
                alturas = request.POST.getlist('altura')
                larguras = request.POST.getlist('largura')
                subtipos_matprima_ids = request.POST.getlist('subtipo_matprima')
                quantidades = request.POST.getlist('quantidade')

                for nome_item, quantidade_x, altura, largura, subtipo_matprima_id, quantidade in zip(nomes_itens, quantidades_x, alturas, larguras, subtipos_matprima_ids, quantidades):
                    # Verificar se os campos de altura e largura estão vazios
                    altura = int(altura) if altura else None
                    largura = int(largura) if largura else None

                    subtipo_matprima = SubTipoMatPrima.objects.get(pk=subtipo_matprima_id)
                    molde_item = MoldeItem(molde=molde, nome=nome_item, quantidade_x=quantidade_x, altura=altura, largura=largura, subtipo_matprima=subtipo_matprima, quantidade=quantidade)
                    molde_item.save()

            # Adicionar mensagem de sucesso
            messages.add_message(request, constants.SUCCESS, 'Molde cadastrado com sucesso!')
        except Exception as e:
            # Em caso de erro, adicione uma mensagem de erro
            messages.add_message(request, messages.ERROR, 'Erro ao cadastrar o molde: {}'.format(str(e)))
        
        # Redirecionar de volta para a mesma página
        return redirect('/molde/add_molde/')

    # Se não for uma requisição POST, redirecione para a página inicial ou renderize um template indicando que a ação não é suportada
    return redirect('/molde/add_molde/')


def carrega_subtipo(request):
    
    subtipos = SubTipoMatPrima.objects.all().values('id', 'nome')  # Obtém os dados da tabela SubTipoMatPrima
    return JsonResponse(list(subtipos), safe=False)

