from datetime import datetime
from decimal import Decimal

from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from administrator.models import (
    FluxoCaixa, FluxoFormPagamento, FluxoFavorecido, FluxoCategoria, FluxoTransacao)
from administrator.forms.formulario_fluxocaixa import (
    FluxoCaixaForm, FluxoFormPagamentoForm, FluxoFavorecidoForm, FluxoCategoriaForm, FluxoTransacaoForm)


# Cadastro da Movimentação
class FluxoCaixaCreateView(CreateView):
    model = FluxoCaixa
    form_class = FluxoCaixaForm
    template_name = 'fluxo_caixa/formulario_fluxocaixa.html'
    success_url = reverse_lazy('listando_movimentacoes')

    def get_context_data(self, **kwargs):
        context = super(FluxoCaixaCreateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Cadastrando Movimentação'
        context['btn_acao'] = 'Cadastrar'

        return context


class FluxoCaixaUpdateView(UpdateView):
    model = FluxoCaixa
    form_class = FluxoCaixaForm
    template_name = 'fluxo_caixa/formulario_fluxocaixa.html'
    success_url = reverse_lazy('listando_movimentacoes')

    def get_context_data(self, **kwargs):
        context = super(FluxoCaixaUpdateView, self).get_context_data(**kwargs)
        context['form'] = FluxoCaixaForm(instance=self.object)
        context['titulo_pagina'] = 'Atualizar Movimentação'
        context['btn_acao'] = 'Atualizar'

        return context

    def post(self, request, *args, **kwargs):
        fluxo_form = FluxoCaixaForm(data=request.POST, instance=self.get_object())
        if fluxo_form.is_valid():
            fluxocaixa = fluxo_form.save(commit=False)
            fluxocaixa.save()

            return HttpResponseRedirect(reverse('listando_movimentacoes'))


class FluxoCaixaDeleteView(DeleteView):
    model = FluxoCaixa
    success_url = reverse_lazy('listando_movimentacoes')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


# Visualização da Movimentação
class FluxoCaixaListView(ListView):
    model = FluxoCaixa
    template_name = 'fluxo_caixa/listando_movimentacoes.html'
    context_object_name = 'fluxo_caixa'
    queryset = FluxoCaixa.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(FluxoCaixaListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Movimentações'

        return context


# Cadastro de Favorecido
class FluxoFavorecidoCreateView(CreateView):
    model = FluxoFavorecido
    form_class = FluxoFavorecidoForm
    template_name = 'fluxo_caixa/formulario_favorecidos.html'
    success_url = reverse_lazy('favorecidos')

    def get_context_data(self, **kwargs):
        context = super(FluxoFavorecidoCreateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Favorecidos'
        context['object_list'] = FluxoFavorecido.objects.all()
        context['btn_acao'] = 'Cadastrar'

        return context


# Cadastro de Forma de Pagamento
class FluxoFormPagamentoCreateView(CreateView):
    model = FluxoFormPagamento
    form_class = FluxoFormPagamentoForm
    template_name = 'fluxo_caixa/formulario_forma_pagamentos.html'
    success_url = reverse_lazy('formas_de_pagamento')

    def get_context_data(self, **kwargs):
        context = super(FluxoFormPagamentoCreateView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Formas de Pagamento'
        context['object_list'] = FluxoFormPagamento.objects.all()
        context['btn_acao'] = 'Cadastrar'

        return context


# Cadastro de Categorias
class FluxoCategoriaView(CreateView):
    model = FluxoCategoria
    form_class = FluxoCategoriaForm
    template_name = 'fluxo_caixa/formulario_categorias.html'
    success_url = reverse_lazy('categorias')

    def get_context_data(self, **kwargs):
        context = super(FluxoCategoriaView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Categorias'
        context['object_list'] = FluxoCategoria.objects.all()
        context['btn_acao'] = 'Cadastrar'

        return context


# Cadastro de Tipos de Movimentação
class FluxoTransacaoView(CreateView):
    model = FluxoTransacao
    form_class = FluxoTransacaoForm
    template_name = 'fluxo_caixa/formulario_tipo_transacao.html'
    success_url = reverse_lazy('tipos_transacao')

    def get_context_data(self, **kwargs):
        context = super(FluxoTransacaoView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Tipo de Transação'
        context['object_list'] = FluxoTransacao.objects.all()
        context['btn_acao'] = 'Cadastrar'

        return context
