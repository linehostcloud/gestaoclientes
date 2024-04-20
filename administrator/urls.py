from django.urls import path

from administrator.views.views_clientes import (
    ClienteCreateView,
    ClienteUpdateView,
    ClienteListView,
    ClienteDetailView,
    ClienteDeleteView
)

from administrator.views.views_fluxocaixa import (
    FluxoCaixaCreateView,
    FluxoCaixaListView
)

urlpatterns = [

    # Clientes
    path('cadastrar_cliente/', ClienteCreateView.as_view(), name='cadastrar_cliente'),
    path('listando_clientes/', ClienteListView.as_view(), name='listando_clientes'),
    path('atualizar_cliente/<int:pk>', ClienteUpdateView.as_view(), name='atualizar_cliente'),
    path('detalhes_cliente/<int:pk>', ClienteDetailView.as_view(), name='detalhes_cliente'),
    path('remover_cliente/<int:pk>', ClienteDeleteView.as_view(), name='remover_cliente'),

    # Pedidos (Fluxo de Caixa)
    path('cadastrar_movimentacao/', FluxoCaixaCreateView.as_view(), name='cadastrar_movimentacao'),
    path('listando_movimentacoes/', FluxoCaixaListView.as_view(), name='listando_movimentacoes'),
]
