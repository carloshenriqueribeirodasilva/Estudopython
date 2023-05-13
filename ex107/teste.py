import moeda

p = float(input('digite um preço R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'diminuir o valor em 10%  {moeda.diminuir(p, 10)}')
print(f'Almentando o valor em 10% {moeda.diminuir(p, 10)}')
