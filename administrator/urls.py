from django.urls import path
from django.views.generic import RedirectView

from administrator.views.views_clientes import (
    ClienteCreateView,
    ClienteUpdateView,
    ClienteListView,
    ClienteDetailView,
    ClienteDeleteView
)

urlpatterns = [

    # Redirecionando
    path('', RedirectView.as_view(), name='listando_clientes'),

    # Clientes
    path('cadastrar_cliente/', ClienteCreateView.as_view(), name='cadastrar_cliente'),
    path('listando_clientes/', ClienteListView.as_view(), name='listando_clientes'),
    path('atualizar_cliente/<int:pk>', ClienteUpdateView.as_view(), name='atualizar_cliente'),
    path('detalhes_cliente/<int:pk>', ClienteDetailView.as_view(), name='detalhes_cliente'),
    path('remover_cliente/<int:pk>', ClienteDeleteView.as_view(), name='remover_cliente'),
]