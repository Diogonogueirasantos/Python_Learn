from random import choice
from collections import namedtuple

"""O objetivo central desse script é criar um jogo de cartas usando o método processual de programação
 (Também conhecido como Método estruturado)"""

# este exemplo inicial é muito parecido com o do livro Fluent em Python

suits = 'Spades Hearts Clubs Diamonds'.split()
rank = [x for x in range(2, 10)] + 'Ace Jack Queen King'.split()

Cards = namedtuple('Deck', ['Suits', 'Rank']) # os campos dentro da lista passam a ser objetos chamados atrvés de cards

deck = [Cards(Suits, Rank) for Suits in suits for Rank in rank]

print(deck)

def select_card_robot():
    robot_1 = choice(deck)
    robot_2 = choice(deck)

    if robot_1.Rank > robot_2.Rank:
        print(f'O robo de número 1 ganhou com o rank de: {robot_1.Rank}')
    elif robot_2.Rank > robot_1.Rank:
        print(f'O robo de número 2 ganhou com o Rank de: {robot_2.Rank}')
    else:
        print('Parece que houve algum erro com a nossas máquina, tente novamente!')

        '''O grande problema aqui é que apesar de sabermos que as cartas Ace, Queen, King e Jack possuem uma ordinalidades entre si, o algoritmo
         não consegui enxergar isso, logo quando um dos robos ou até mesmo ambos escolherem esta carta ocorrerá erro.
         Uma maneira simples de se resolver isso é atribuir peso comparativo entre as cartas.'''


select_card_robot()

# explorar mais o módulo nametuple, ele parece promissor!