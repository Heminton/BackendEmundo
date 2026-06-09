from django.urls import path, include

urlpatterns = [
    
    path('departamentos/', include('apps.catalogos.departamento.urls')),
    path('clientes/', include('apps.catalogos.cliente.urls')),
]