def notas(*n, sit=False):
    """
    -> Função para analizar a nota de varios alunos.
    :param n: uma ou mais nota
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com vairias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['mior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)

#help(notas)

