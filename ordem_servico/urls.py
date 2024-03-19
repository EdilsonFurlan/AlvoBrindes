from django.urls import path
from . import views

urlpatterns = [
    path('add_ordem_servico/',views.add_ordem_servico,name='add_ordem_servico_url'),
    path('salvar_ordem_servico/',views.salvar_ordem_servico, name='salvar_ordem_servico_url'),
    path('adicionar_combobox/',views.adicionar_combobox,name='adicionar_combobox_url'),
    path('calcula_total/',views.calcula_total, name='calcula_total_url'),
]
