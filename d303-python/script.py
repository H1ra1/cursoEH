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

# print('Insira seu salario:')
# salario = input()
# print('Qual valor do emprestimo?')
# emprestimo = input()
# print('Parcelar em quantas vezes?')
# qtdParcelas = input()

if nome:
    print('Insira sua idade:')
    idade = input()
    if idade >= 25 and idade <= 55:
      print('ok')  
    else:
        print('Idade invalida')
else: 
    print('insira seu nome')

