n = str(input('Digite seu nome completo: ')).strip() # STRIP REMOVE OS ESPAÇOS CASO O USUARIO DE ESPAÇOS ANTES DAS FRASE
nome = n.split() # SPLIT TRANSFORMA A FRASE EM LISTAS [] E SEPARA AS PALAVRAS
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) # Analiza as palavras dentro das listas, -1 pega a ultima frase
