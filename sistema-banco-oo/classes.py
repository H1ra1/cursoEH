from random import randint
import json

class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Conta:
    def __init__(self, cliente):
        self.titular = cliente
        self.numero = self.gerar()
        self.saldo = 0

    def extrato(self):
        print(f'Numero: {self.numero}\nSaldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor

    def transferir(self, conta, valor):
        retirar = self.sacar(valor)
        if(retirar == False):
            return False
        else:
            conta.depositar(valor)

    def gerar(self):
        self.random_num = f'{randint(1000, 9999)}-{randint(1, 9)}'
        return self.random_num


