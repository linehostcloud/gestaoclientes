from django.db import models


# ENDEREÇO
class Endereco(models.Model):
    ESTADO_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'),
    )
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True, choices=ESTADO_CHOICES)
    cep = models.CharField(max_length=9, null=True, blank=True)

    class Meta:
        db_table = 'endereco'


# CLIENTES
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    celular = models.CharField(max_length=16, null=True, blank=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    endereco = models.OneToOneField(to=Endereco, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


# FLUXO DE CAIXA - CATEGORIA
class FluxoCategoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)


# FLUXO DE CAIXA - TIPO DE TRANSAÇÃO
class FluxoTransacao(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)


# FLUXO DE CAIXA - FORMA DE PAGAMENTO
class FluxoFormaPagamento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)


# FLUXO DE CAIXA - FAVORECIDO
class FluxoFavorecido(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)


# FLUXO DE CAIXA - MODELO
class FluxoCaixa(models.Model):
    transacao = models.ForeignKey(to=FluxoTransacao, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_movimentacao = models.DateField(null=False, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    cliente = models.ForeignKey(to=Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(to=FluxoCategoria, on_delete=models.SET_NULL, null=True, blank=True)
    forma_pagamento = models.ForeignKey(to=FluxoFormaPagamento, on_delete=models.SET_NULL, null=True, blank=True)
    favorecido = models.ForeignKey(to=FluxoFavorecido, on_delete=models.SET_NULL, null=True, blank=True)
    pago = models.BooleanField(default=False)
    descricao = models.TextField(null=True, blank=True)
