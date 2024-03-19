from django.urls import path
from .import views

urlpatterns = [
    path('add_cliente/',views.add_cliente,name='add_cliente_url'),
    path('criar_cliente/',views.criar_cliente,name='criar_cliente'),
    
]

