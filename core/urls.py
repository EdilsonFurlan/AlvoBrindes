from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('produto/',include('produto.urls')),
    path('produto_variavel/',include('produto_variavel.urls')),
    path('molde/',include('molde.urls')),
    path('ordem_servico/',include('ordem_servico.urls')),
    path('cliente/',include('cliente.urls')),
    path('pedido/',include('pedido.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
