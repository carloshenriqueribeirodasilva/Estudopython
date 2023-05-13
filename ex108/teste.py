import moeda

p = float(input('digite um preço R$ '))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p)}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p)}')
print(f'diminuir o valor em 10%  R${moeda.diminuir(p, 10)}')
print(f'Almentando o valor em 10% R${moeda.diminuir(p, 10)}')
