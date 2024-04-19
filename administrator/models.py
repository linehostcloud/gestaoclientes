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
    DOCUMENTO_CHOICES = (
        ('CPF', 'CPF'),
        ('CNPJ', 'CNPJ'),
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    celular = models.CharField(max_length=16, null=True, blank=True)
    documento = models.CharField(max_length=4, choices=DOCUMENTO_CHOICES, null=True, blank=True)
    endereco = models.OneToOneField(to=Endereco, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
