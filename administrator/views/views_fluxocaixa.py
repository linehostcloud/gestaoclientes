from datetime import datetime
from decimal import Decimal

from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from administrator.models import FluxoCaixa
from administrator.forms.formulario_fluxocaixa import FluxoCaixaForm


# View de Cadastro
class FluxoCaixaCreateView(CreateView):
    model = FluxoCaixa
    form_class = FluxoCaixaForm
    template_name = 'fluxo_caixa/formulario_fluxocaixa.html'
    success_url = reverse_lazy('listando_fluxo_caixa')

    def get_context_data(self, **kwargs):
        context = super(FluxoCaixaCreateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Cadastrando Movimentação'
        context['btn_acao'] = 'Cadastrar'

        return context


class FluxoCaixaListView(ListView):
    model = FluxoCaixa
    template_name = 'fluxo_caixa/listando_movimentacoes.html'
    context_object_name = 'fluxo_caixa'
    queryset = FluxoCaixa.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(FluxoCaixaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Movimentações'

        return context
