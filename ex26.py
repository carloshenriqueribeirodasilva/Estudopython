frase = str(input('Digite uma frase: ')).upper().strip() # UPPER DEIXA TODAS AS LETRAS EM MAIUSCULAS / STRIP ELIMINA TODOS OS ESPAÇOS
print('A letra A aparece {} vezes na frase.'.format(frase.count('A'))) #COUNT CONTABILIZA QUANTAS VEZES A LETRA APARECEU NA FRASE
print('A primeira letra A apareceu na posição {}'.format(frase.find('A'))) # FIND PROCURA A POSIÇÃO EM QUE A LETRA APARECE PELA PRIMEIRA VEZ
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A'))) # RFIND PROCURA A POSIÇÃO QUE A LETRA APARECE PELA PRIMEIRA VEZ NA FRASE / DA DIREITA PRA ESQUERDA
