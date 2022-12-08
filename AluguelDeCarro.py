km = float(input('qual a quantidade de km percorrido? '))
dias = int(input('qual a quantidade de dias voce ficou com o carro? '))

km = km * 0.15
dias = dias * 60
total = dias + km

print('O valor por km percorrido é {} o valor da quantidade de dias é {}'.format(km, dias))
print('o tota a se pagar é R${:.2f}'.format(total))
