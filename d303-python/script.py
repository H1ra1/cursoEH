# print('Insira o material da escada:')
# material = input()
# print('Insira a quantidade de escadas:')
# count = 0
# qnt = int(input())
# desenhar = ''

# while count < qnt:
#     desenhar += material
#     print(desenhar)
#     count += 1

print('Insira seu nome:')
nome = input()



# print('Parcelar em quantas vezes?')
# qtdParcelas = input()

if nome:
    print('Insira sua idade:')
    idade = int(input())
    if idade >= 25 and idade <= 55:
        print('Insira seu salario:')
        salario = int(input())
        if salario >= 1000:
            print('Qual valor do emprestimo?')
            emprestimo = int(input())
            if emprestimo <= salario * 15:
                print(f'Ola, {nome}. Seu emprestimo de {emprestimo} foi aprovado')
            else:
                print('Seu emprestimo foi negado pois ultrapassa o valor maximo')
        else: 
            print('salario insuficiente')
    else:
        print('Idade invalida')
else: 
    print('insira seu nome')