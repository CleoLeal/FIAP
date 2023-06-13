umidadeGravimetrica = 0
#função para calcular a umidade Gravimetrica
def Umidade_Gravimetrica(solo_umido:float, solo_seco:float) -> int:
    umidadeGravimetrica = ((solo_umido - solo_seco) / solo_seco) * 100 #a função que é capaz de calcular a umidade. O resultado é em porcentagem
    return umidadeGravimetrica.__trunc__() #retorna o resultado da função

def Consultar(lista_resultados:list):
    # formata o vetor com símbolo de %
    resultados_formatados = [f"{resultado}%" for resultado in lista_resultados]
    return ', '.join(resultados_formatados)  # ele une em uma única str, separando por vírgula e espaço