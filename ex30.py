n = int(input('Digite um numero para saber se ele é IMPAR ou PAR!: '))
resultado = n % 2 # O RESTO DE QUALQUER NUMERO SEMPRE VAI DAR 0 OU 1
if resultado == 0:
    print('O numero {} é PAR!'.format(n))
else:
    print('O numeor {} é IMPAR!'.format(resultado))

