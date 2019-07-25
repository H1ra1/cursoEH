from classes import Cliente, Conta

class CaixaEletronico():
    def __init__(self):
        self.nome = input('Digite seu nome: ')
        self.cpf = input('Digite seu cpf: ')

        cliente = Cliente(self.nome, self.cpf)
        self._conta = Conta(cliente)

        print(f'Olá, {self._conta.titular.nome}, sua conta é: {self._conta.numero}')

    def exibir_menu(self):
        print('1- Consultar saldo\n2- Depositar\n3- Sacar')
        escolha = input('Escolha uma opção')

        if escolha == '1':
            self.exibir_saldo()
        elif escolha == '2':
            pass
        else: 
            print('Opção inválida')

    def exibir_saldo(self):
        valor = self._conta.exibir_saldo()
        print(f'Seu saldo é: {valor}')
            


    


