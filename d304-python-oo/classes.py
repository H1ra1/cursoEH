from random import randint
import json

# class Criar():
#     def __init__(self, nome, cpf, senha, dinheiro):
#         self.nome = {
#             "nome": nome,
#             "cpf": cpf,
#             "senha": senha,
#             "dinheiro": dinheiro,
#             "num": self.gerar_numero()
#         }
    
#     def gerar_numero(self):
#         self.numero = f'{randint(1000, 9999)}-{randint(1, 9)}'
#         return str(self.numero)

#     def __str__(self):
#         return f'{json.dumps(self.nome)}'
            
# class Conta():
#     def __init__(self):
#         self.contas = {}
        
#     def inserir_conta(self, conta):
#         self.obj = json.loads(conta)
#         self.contas[self.obj['nome']] = conta

#     def informar_conta(self, nome):
#         conta_convert = json.loads(self.contas[nome])
#         return conta_convert

#     def acessar_conta(self, nome, num):
#         conta_convert = json.loads(self.contas[nome])
#         return conta_convert

#     def saldo(self, nome):
#         conta_convert = json.loads(self.contas[nome])
#         return conta_convert['dinheiro']

#     def depositar(self, nome, valor):
#         conta_convert = json.loads(self.contas[nome])
#         soma = int(conta_convert['dinheiro']) + int(valor)
#         conta_convert['dinheiro'] = soma
#         return conta_convert['dinheiro']

#     def sacar(self, nome, valor):
#         conta_convert = json.loads(self.contas[nome])
#         sub = int(conta_convert['dinheiro']) - int(valor)
#         conta_convert['dinheiro'] = sub
#         return conta_convert['dinheiro']

class Pessoa():
    def criar_pessoa(self, nome, idade, cpf):
        pessoa = {
            "nome": nome,
            "idade": idade,
            "cpf": cpf
        }

        return pessoa

class Conta():
    def criar_conta(self, pessoa, saldo, numero_conta, senha):
        conta = {
            "nome": pessoa['nome'],
            "idade": pessoa['idade'],
            "cpf": pessoa['cpf'],
            "saldo": saldo,
            "numero_conta": numero_conta,
            "senha": senha
        }

        return conta

    def gerar_numero(self):
        self.numero = f'{randint(1000, 9999)}-{randint(1, 9)}'

        return str(self.numero)

    def adicionar_conta(self, conta):
        contas = {
            conta['nome']: {
                conta
            }
        }

        return contas

class Operacoes():
    def __init__(self, conta):
        self.conta = conta
    
    def acessar_conta(self):
        self.nome = json.loads(self.conta['nome'])

    def saldo(self):
        self.dinheiro = json.loads(self.conta['saldo'])

        return self.dinheiro
    
    def sacar(self, valor):
        self.dinheiro = json.loads(self.conta['saldo'])
        self.novo_saldo = int(self.dinheiro) - int(valor)
        self.conta['saldo'] = self.novo_saldo

        return str(self.conta['saldo'])