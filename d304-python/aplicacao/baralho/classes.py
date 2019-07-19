from random import randint

NAIPES = ('Paus', 'Copas', 'Espadas', 'Ouros')
RANKS = ('As', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei')


class Carta():
    def __init__(self, naipe, rank, valor):
        self.naipe = naipe
        self.rank = rank
        self.valor = valor
        
    def __str__(self):
        return f'{self.rank}({self.valor}) de {self.naipe}'

class Baralho():
    def __init__(self):
        self.cartas = []

        for naipe in NAIPES:
            for rank in RANKS:
                carta = Carta(naipe, rank, 1)
                self.adicionar_carta(carta)

    def __str__(self):
        if len(self.cartas) == 0:
            return '[VAZIO]'
        
        string = ''

        for carta in self.cartas:
            string += str(carta)
            string += '\n'

        return string

    def adicionar_carta(self, carta):
        self.cartas.append(carta)
    
    def remover_carta(self):
        return self.cartas.pop()

    def sortear_carta(self):
        numero_sorteado = randint(0, len(self.cartas) - 1)
        return self.cartas.pop(numero_sorteado)

class Jogo21():
    def __init__(self):
        baralho = Baralho()
        carta1  = baralho.sortear_carta()
        carta2 = baralho.sortear_carta()