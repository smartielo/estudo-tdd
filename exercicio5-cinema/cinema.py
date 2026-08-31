def calcular_ingresso(idade, estudante):
    preco_padrao = 30
    if idade <= 0:
        raise ValueError("A idade deve ser maior que 1.")
    if 12 <= idade <= 60 or estudante == True:
        ingresso = preco_padrao / 2
    else:
        ingresso = preco_padrao
    return ingresso


def comprar_lanche(tipo_lanche):
    if tipo_lanche == "Pipoca":
        valor_lanche = 20 
    elif tipo_lanche == "Refrigerante":
        valor_lanche = 10
    elif tipo_lanche == "Combo":
        valor_lanche = 25
    else:
        raise ValueError ("Digite um lanche válido. ")
    return valor_lanche

def fechar_pedido(idade, estudante, tipo_lanche=None):
    ...