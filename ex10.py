d = int(input("Quanto de dinheiro você tem na carteira? R$:  "))
dolar = 5.26
valor = d / dolar
print("Com R${} você pode compar U${:.2f}".format(d, valor))
