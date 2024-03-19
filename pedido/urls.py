from django.urls import path
from .import views

urlpatterns = [
    
    path('add_pedido/',views.add_pedido,name='add_pedido_url'),
]
