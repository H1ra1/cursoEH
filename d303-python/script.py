from random import randint

# ESCADAS ==>

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


# EMPRESTIMO ==>

# print('Insira seu nome:')
# nome = input()
# print('Insira sua idade:')
# idade = int(input())
# print('Insira seu salario:')
# salario = int(input())
# print('Qual valor do emprestimo?')
# emprestimo = int(input())
# print('Parcelar em quantas vezes?')
# qtdParcelas = input()

# if nome == '':
#     print('Preencha o campo nome')
# elif idade < 21 or idade > 55:
#         print('Idade não aceita')
# elif salario <= 1000:
#         print('salario abaixo do desejado')
# elif emprestimo >= salario * 15:
#         print('emprestimo acima do limite')
# else:
#     print(f'Ola {nome}, o emprestimo no valor de: {emprestimo} foi aprovado')

# EMBARALHAR ==>

# arr = [1, 2, 3, 4, 6, 7, 8]

# def embaralhar(lista):
#     indice_atual = len(lista)
#     valor_temporario = None
#     indice_aleatorio = None
#     count = 0

#     while count != indice_atual:
#         indice_aleatorio = randint(0, indice_atual)
#         indice_atual -= 1

#         valor_temporario = lista[indice_atual]
#         lista[indice_atual] = lista[indice_aleatorio]
#         lista[indice_aleatorio] = valor_temporario

#     return print(lista)

# embaralhar(arr)

# FUNCOES QUADRILHA ==>

meninos = ['jotinha', 'JonyBoy', 'Zézinho', 'Seucuca', 'Faustinho', 'Jorgin']
meninas = ['Nina', 'Felipinha', 'Fabi', 'Nica', 'Juriscreuza', 'Betina', 'Padawana', 'Judite']

def casais(lis1, lis2):
    if len(lis1) > len(lis2):
        lista = lis2
        lista_maior = lis1
        indice = len(lis2) -1
        stop = len(lis1) - len(lis2)
        
    else:
        lista = lis1
        lista_maior = lis2
        indice = len(lis1) - 1
        stop = len(lis2) - len(lis1)

    for i in range(len(lista)):
        casais = f'Casal {i + 1} -> {lis1[i]} e {lis2[i]}'
        print(casais)
    count = 0
    while count < stop:
        indice += 1
        print(f'Sem par -> {lista_maior[indice]}')
        count += 1
        


casais(meninos, meninas)







