def soma(num1,num2, *args):
    pontos = num1 +num2
    for arg in args:
        pontos += arg
    return pontos

def pontuacao_total(pontos, **kwargs):
    pontos_multiplicador = kwargs.get('multiplicador')
    pontos_bonus = kwargs.get('bonus')

    if pontos_bonus:
        pontos += pontos_bonus
    if pontos_multiplicador:
        pontos *= pontos_multiplicador
    

    return f"Pontuacao final: {pontos}"

pontuacao_final = pontuacao_total(100.01, bonus=500.2)
print(pontuacao_final)

pontuacao_final = pontuacao_total(100.01,multiplicador=10)
print(pontuacao_final)


