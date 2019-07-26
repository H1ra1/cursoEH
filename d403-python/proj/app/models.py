from django.db import models

# Create your models here.
class Pessoa(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )

    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome'
        )
        
    cpf = models.CharField(
        max_length = 255,
        verbose_name = 'CPF'
        )

    email = models.EmailField(
        max_length = 255,
        verbose_name = 'E-mail'
    )

    telefone = models.CharField(
        max_length = 255,
        verbose_name = 'Telefone'
    )

    genero = models.CharField(
        max_length = 255,
        verbose_name = 'Genero',
        choices = GENEROS
    )

    ativo = models.BooleanField(
        default = True
    )

    data_de_criacao = models.DateField(
        auto_now_add = True
    )

    def __str__(self):
        return f'({self.id}) {self.nome}'

class Conta(models.Model):
    pessoa = models.ForeignKey(
        Pessoa, on_delete = models.CASCADE
    )

    agencia = models.CharField(
        max_length = 255,
        verbose_name = 'Agencia'
    )

    nome_banco = models.CharField(
        max_length = 255,
        verbose_name = 'Nome do banco',
        default = 'LiraBank',
        null = True
    )

    numero_conta = models.CharField(
        max_length = 255,
        verbose_name = 'Numero da conta'
    )

    saldo = models.FloatField(
        default = 0.0
    )