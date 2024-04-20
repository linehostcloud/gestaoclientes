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
    FluxoCaixaListView,
    FluxoCaixaDeleteView,
    FluxoFormPagamentoCreateView,
    FluxoFavorecidoCreateView,
    FluxoCategoriaView,
    FluxoTransacaoView,
    FluxoCaixaUpdateView
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
    path('formas_de_pagamento/', FluxoFormPagamentoCreateView.as_view(), name='formas_de_pagamento'),
    path('favorecidos/', FluxoFavorecidoCreateView.as_view(), name='favorecidos'),
    path('categorias/', FluxoCategoriaView.as_view(), name='categorias'),
    path('tipos_transacao/', FluxoTransacaoView.as_view(), name='tipos_transacao'),
    path('atualizar_movimentacao/<int:pk>', FluxoCaixaUpdateView.as_view(), name='atualizar_movimentacao'),
    path('excluir_movimentacao/<int:pk>', FluxoCaixaDeleteView.as_view(), name='excluir_movimentacao'),
]
