from django.shortcuts import render,redirect
from .models import Cliente

def add_cliente(request):

    clientes = Cliente.objects.all()

    return render(request, 'add_cliente2.html',{'clientes':clientes})

from django.shortcuts import render, redirect
from .forms import ClienteForm

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nome_da_view')  # Redirecionar para a página desejada após salvar o cliente
    else:
        form = ClienteForm()
    return render(request, 'add_cliente.html', {'form': form})