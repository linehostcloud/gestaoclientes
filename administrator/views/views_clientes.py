from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from administrator.models import Cliente
from administrator.forms.formulario_cliente import ClienteForm, EnderecoForm

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class ClienteCreateView(CreateView):
    form_class = ClienteForm
    template_name = 'clientes/formulario_cliente.html'
    success_url = 'listando_clientes'

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context['form'] = ClienteForm()
        context['endereco_form'] = EnderecoForm()
        context['titulo_pagina'] = 'Cadastro de Clientes'
        context['btn_acao'] = 'Cadastrar'

        return context

    def post(self, request, *args, **kwargs):
        cliente_form = ClienteForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        if cliente_form.is_valid() and endereco_form.is_valid():
            cliente = cliente_form.save(commit=False)
            endereco = endereco_form.save()
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse('listando_clientes'))


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/listando_clientes.html'
    queryset = Cliente.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listando Clientes'  # Título da Página
        context['btn_acao'] = 'Cadastrar'  # Título do botão

        return context


# Atualizando o cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/formulario_clientes.html'
    success_url = reverse_lazy('listando_clientes')

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        context['form'] = ClienteForm(instance=self.object)
        context['endereco_form'] = EnderecoForm(instance=self.object.endereco)
        context['titulo_pagina'] = 'Editando Cliente'  # Título da Página
        context['btn_acao'] = 'Atualizar'  # Título do botão

        return context

    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs['pk'])
        cliente_form = ClienteForm(data=request.POST or None, instance=cliente)
        endereco_form = EnderecoForm(data=request.POST or None, instance=cliente.endereco)
        if cliente_form.is_valid() and endereco_form.is_valid():
            cliente = cliente_form.save(commit=False)
            endereco = endereco_form.save()
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse('listando_clientes'))


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/detalhes_clientes.html'
    context_object_name = 'cliente'  # mudando o nome do object_list

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['cliente'] = Cliente.objects.select_related('endereco').get(id=self.kwargs['pk'])
        context['titulo_pagina'] = 'Detalhes do Cliente'  # Título da Página

        return context


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/remover_cliente.html'
    success_url = reverse_lazy('listando_clientes')

    def get_context_data(self, **kwargs):
        context = super(ClienteDeleteView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Excluir Cliente'  # Título da Página
        context['btn_acao'] = 'Excluir'  # Título do botão

        return context

    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs['pk'])
        cliente.endereco.delete()
        cliente.delete()

        return HttpResponseRedirect(reverse('listando_clientes'))
