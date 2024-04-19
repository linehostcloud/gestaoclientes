from django import forms
from django.forms import ModelForm
from administrator.models import Cliente, Endereco
from pycpfcnpj import cpfcnpj


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'email', 'celular', 'cnpj', 'cpf']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for camposForms in self.fields:
            #  Ocultando a label dos formulários de cadastro dos clientes
            self.fields[camposForms].label = ""

            #  Modificando o placeholder padrão dos inputs
            self.fields[camposForms].widget.attrs.update({
                'class': 'formClient',
                'placeholder': {
                    'nome': 'Nome',
                    'sobrenome': 'Sobrenome',
                    'email': 'Digite um e-mail válido',
                    'celular': 'WhatsApp',
                    'cnpj': 'CNPJ',
                    'cpf': 'CPF',
                }[camposForms]
            })

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if cpf is not None:
            cpf = cpf.replace(".", "").replace("-", "")
            if not cpfcnpj.validate(cpf):
                raise forms.ValidationError("O CPF informado é inválido!")
        return cpf

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        if cnpj is not None:
            cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
            if not cpfcnpj.validate(cnpj):
                raise forms.ValidationError("O CNPJ informado é inválido!")
        return cnpj


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado']

    def __init__(self, *args, **kwargs):
        super(EnderecoForm, self).__init__(*args, **kwargs)
        for enderecoCampos in self.fields:
            self.fields[enderecoCampos].label = ""
            self.fields[enderecoCampos].widget.attrs.update({
                'class': 'formEndereco',
                'placeholder': {
                    'rua': 'Rua',
                    'numero': 'Número',
                    'complemento': 'Complemento',
                    'bairro': 'Bairro',
                    'cidade': 'Cidade',
                    'cep': 'CEP',
                    'estado': 'Estado',
                }[enderecoCampos]
            })
