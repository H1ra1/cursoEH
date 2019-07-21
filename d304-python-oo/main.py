from classes import Criar, Conta

contas = Conta()

# criar = Criar('teste', 'teste', 'teste', 'teste')
# conta = f'{criar}'
# criar2 = Criar('teste2', 'teste2', 'teste2', 'teste2')
# conta2 = f'{criar2}'
# contas = Contas()
# contas.inserir_conta(conta)
# contas.inserir_conta(conta2)
# print(contas.acessar_conta('teste2'))

def interface():
    print('Bem vindo ao banco Mastertech.\n\nSelecione a operação desejada ->')

    opr = input('Criar conta(1) | Acessar conta(2) | Sair(3): ')

    if opr == '1':
        print('\nCiar nova conta ->\n')
        nome = input('Insira seu nome: ')
        cpf = input('Insira seu CPF: ')
        senha = input('Insira sua senha: ')
        dinheiro = input('Faça seu primeiro deposito: ')
        criar = Criar(nome, cpf, senha, dinheiro)
        conta = f'{criar}'
        contas.inserir_conta(conta)
        info = contas.informar_conta(nome)
        print('\nConta criada com sucesso!\n')
        print(f'Olá {info["nome"]}, sua conta é {info["num"]}\n')

        return interface()
    elif opr == '2':
        nome = input('informe seu nome: ')
        num = input('Informe o numero da sua conta: ')
        info = contas.informar_conta(nome)

        if info['num'] == num:
            acesso = contas.acessar_conta(nome, num)
            print(f'\nOlá {acesso["nome"]}\n')
            print('1- Consultar saldo\n2- Depositar\n3- Sacar\n')
            choice = input(': ')
            if choice == '1':
                acesso = contas.saldo(nome)
                print(f'\nSeu saldo é: {acesso}\n')

                return interface()
            elif choice == '2':
                valor = input('\nDigite o valor: ')
                acesso = contas.depositar(nome, valor)
                print(f'\nDepósito efetuado. Seu novo saldo é R$ {acesso}')

                return interface(), contas.depositar(nome, valor)
            elif choice == '3':
                valor = input('\nDigite o valor: ')
                acesso = contas.sacar(nome, valor)
                print(f'\nSaque efetuado. Seu novo saldo é R$ {acesso}')
            else:
                print('\n-Insira uma operação válida-\n')
                    
                return interface()
        else:
            print('\n-Numero inválido-\n')
            return interface()
           
    elif opr == '3':
        print('\nAté logo!\n')
        return
    else:
        print('Selecione uma operação válida! \n')
        return interface()

interface()




