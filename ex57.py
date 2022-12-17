sexo = str(input('Digite seu sexo: ')).strip().upper()[0] # STRIP ELIMINA OS ESPAÇOS, UPPER DEIXA TODAS AS LETRAS EM MAIUSCULAS [0] PEGA A PRIMEIRA LETRA
while sexo not in 'MF': # ENQUANTO NA VARIAVEL SEXO NAO TIVER TIVER A LETRA M OU F NAO PARE
    sexo = str(input('sexo invalido tente novamente: ')).strip().upper()[0]
print('Sexo valido')
