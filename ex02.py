nome = str(input("Digite seu nome: ")).strip()
cores = {'limpa' : '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033{33m',
         'pretoebranco': '\033[7;30m'}
print("É um prazer te conhecer, {}{}{}!".format(cores['azul'], nome, cores['limpa']))



