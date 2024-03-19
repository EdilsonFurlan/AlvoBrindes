from django.urls import path
from .import views

urlpatterns = [
    path('adicionar_produto/', views.adicionar_produto,name='adicionar_produto'),
    path('buscar_molde_itens/<int:id_molde>/',views.buscar_molde_itens,name='buscar_molde_itens'),
    path('buscar_matprima_tipo/<int:id_tipo>/',views.buscar_matprima_tipo,name='buscar_matprima_tipo'),
    path('salvar_produto/',views.salvar_produto,name='salvar_produto'),
    
    
]
