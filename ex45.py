from random import randint # RANDINT SERVE PARA O COMPUTADOR SORTEAR UM NUMERO DENTRO DE UM ITEM
from time import sleep # SERVE PARA TEMPORIZAR ALGO, NO CASO FOI UTILIZADO PARA ATRAZAR EM 1 SEGUNDO A PALAVRA JO KEN PO

print('SUAS OPÇÕES:')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
itens = ('PEDRA', 'PAPEL', 'TESOURA') # ITENS FOI CRIADO PARA O COMPUTADOR SORTEAR UM ITEM (PEDRA, PAPEL, TESOURA)
computador = randint(0, 2) # COMPUTADOR SORTEIA UM ITEM ENTRE ( 0 1 2) DENTRO DE ITENS.       0      1       2
print('JO')
sleep(1) # SLEEP ATRASA A PALAVRA EM 1 SEGUNGO
print('KEN')
sleep(1) # SLEEP ATRASA A PALAVRA EM 1 SEGUNGO
print('PO')
sleep(1) # SLEEP ATRASA A PALAVRA EM 1 SEGUNGO
print('=-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('=-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
         print('JOGADOR GANHOU')
    elif jogador == 2:
         print('COMPUTADOR GANHOU')

elif computador == 1:
    if jogador == 0:
         print('COMPUTADOR GANHOU')
    elif jogador == 1:
            print('EMPATOU')
    elif jogador == 2:
         print('JOGADOR GANHOU')

elif computador == 2:
    if jogador == 0:
            print('JOGADOR GANHOU')
    elif jogador == 1:
            print('COMPUTADOR GANHOU')
    elif jogador == 2:
            print('EMPATOU')




