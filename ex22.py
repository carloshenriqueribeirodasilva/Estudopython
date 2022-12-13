nome = str(input("Digite seu nome completo: ")).strip() # strip elimina os spaços entre os nomes
print("Analizando seu nome....")
print("Seu nome em maiusculas é {}".format(nome.upper())) # upper analiza letras maiusculas
print("Seu nome em minuscula é {}".format(nome.lower())) # lower analiza letras minusculas
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" "))) #len analiza o comprimento do nome #count nao conta os espaços
print("Seu primeiro nome tem {}".format(nome.find(" "))) # find conta quantas letras tem no primeiro nome

