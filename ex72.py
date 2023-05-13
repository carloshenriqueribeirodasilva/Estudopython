cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
         'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero: '))
    print(f'Voce digitou o numero {cont[num]}')
    if -1 <= num >= 20:
        break
        print('Tente novamente. ')









