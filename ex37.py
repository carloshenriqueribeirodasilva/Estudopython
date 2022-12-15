#num = int(input('Digite um número inteiro: '))
num = 22334
print('''Escolha uma das bases para conversão dos numero 22334:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIOO é igual a {}'.format(num, bin(num)[2:])) # bin converte o numero para binario
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:])) # oct converte o numero para octal
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:])) # hex converte o numero para hexadecimal
else:
    print('Digite uma opção valida! Tente novamente.')