# LIMITE DE VOLOCIDADE, SE ULTRAPASSAR LEVA UMA MULTA DE 7 POR KM ULTRAPASSADO

velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    print('MULTADO! você excedeu o limite permitido que é de 80KM/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia, Dirija com segurança!')

