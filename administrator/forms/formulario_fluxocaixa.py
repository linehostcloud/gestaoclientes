from django import forms
from django.forms import ModelForm
from tinymce.widgets import TinyMCE

from administrator.models import FluxoCaixa


class FluxoCaixaForm(ModelForm):
    class Meta:
        model = FluxoCaixa
        fields = ['data_movimentacao', 'transacao', 'nome', 'valor', 'cliente', 'categoria', 'forma_pagamento', 'forma_pagamento', 'pago',
                  'descricao', 'favorecido']
        widgets = {
            'data_movimentacao': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'descricao': TinyMCE(attrs={
                'cols': 80,
                'rows': 10,
            }),
        }

    def __init__(self, *args, **kwargs):
        super(FluxoCaixaForm, self).__init__(*args, **kwargs)

        replace_labels = {
            'data_movimentacao': 'Data da Movimentação',
            'transacao': 'Tipo de Movimentação',
            'nome': 'Nome da Movimentação',
            'valor': 'Valor da Movimentação',
            'cliente': 'Cliente Relacionado',
            'categoria': 'Categoria da Movimentação',
            'forma_pagamento': 'Forma de Pagamento',
            'favorecido': 'Favorecido',
            'pago': 'Esse pedido foi pago?',
            'descricao': 'Anotações',
        }

        for camposFluxoCaixa in self.fields:
            self.fields[camposFluxoCaixa].label = replace_labels[camposFluxoCaixa]
            self.fields[camposFluxoCaixa].widget.attrs.update({
                'class': 'formFluxoImput',
                'placeholder': {
                    'data_movimentacao': 'Data da Movimentação',
                    'transacao': 'Tipo de Movimentação',
                    'nome': 'Nome da Movimentação',
                    'valor': 'Valor da Movimentação',
                    'cliente': 'Cliente Relacionado',
                    'categoria': 'Categoria da Movimentação',
                    'forma_pagamento': 'Forma de Pagamento',
                    'favorecido': 'Favorecido',
                    'pago': 'Esse pedido foi pago?',
                    'descricao': 'Anotações',
                }[camposFluxoCaixa]
            })
            if self.instance.pk:

                valor = getattr(self.instance, camposFluxoCaixa)
                if valor:
                    self.fields[camposFluxoCaixa] = valor.strftime('%Y-%m-%d')
                else:
                    self.fields[camposFluxoCaixa].widget.attrs['class']: 'camposFluxoCaixa'
