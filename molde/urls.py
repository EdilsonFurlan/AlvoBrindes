from django.urls import path
from.import views

urlpatterns = [
    path('add_molde/',views.add_molde,name='add_molde'),
    path('salvar_molde/',views.salvar_molde,name='salvar_molde'),
    path('salvar_molde/',views.salvar_molde,name='salvar_molde_url'),
    path('carrega_subtipo/',views.carrega_subtipo,name='carrega_subtipo_url'),
]
