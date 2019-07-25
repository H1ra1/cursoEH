from classes import Cliente, Conta

nome = input('Insira seu nome: ')
cpf = input('insira seu cpf: ')
idade = input('insira sua idade: ')
valor = input('Faça o primeiro deposito: ')

cliente = Cliente(nome, cpf, idade)
conta = Conta(cliente)
conta.depositar(int(valor))
conta.extrato()


