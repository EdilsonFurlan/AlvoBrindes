from django.urls import path
from .import views

urlpatterns = [
    path('add_produto_variavel/',views.add_produto_variavel,name='add_produto_variavel'),
    path('buscar_produto_itens/<int:produto_id>/', views.buscar_produto_itens, name='buscar_produto_itens_url'),
    path('buscar_matprima/<int:tipo_id>/',views.buscar_matprima, name='buscar_matprima_url'),
    path('salvar_produto_variavel/',views.salvar_produto_variavel, name='salvar_produto_variavel_url'),
]
