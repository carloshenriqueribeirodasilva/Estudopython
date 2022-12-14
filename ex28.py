from random import randint # O COMPUTADOR PENSAR EM UM NUMERO ALEATORIO
computador = randint(0, 5) # FAZ O COMPUTADOR SORTEAR UM NUMERO DE 0 A 5
print('Vou pensar em um numero entre 0 a 5, tente adinvinhar: ')
jogador = int(input('Em qual numero pensei? '))
if jogador == computador:
    print('PARABENS VOCÊ VENCEU')
else:
    print('VOCÊ PERDEU, EU PENSEI NO NUMERO {} E NAO NO NUMERO {}'.format(computador, jogador))
