carrinho = []

def calcular_subtotal(carrinho):
    if carrinho is None or len(carrinho) == 0:
        raise ValueError("O carrinho não pode estar vazio.")
    subtotal = 0
    for item in carrinho:
        if item <= 0:
            raise ValueError("O valor do item não pode ser negativo.")
        subtotal += item
    return subtotal

def aplicar_cupom(valor, cupom):
    if cupom is None or cupom == "":
        raise ValueError("O cupom não pode ser vazio.")
    if cupom == "DESC10":
        return valor * 0.9
    elif cupom == "DESC20":
        return valor * 0.8
    elif cupom == "SEMANA30":
        return valor * 0.7
    else:
        raise ValueError("Cupom inválido.")

def calcular_compra (precos, cupom=None):
    subtotal = calcular_subtotal(precos)
    if cupom:
        total = aplicar_cupom(subtotal, cupom)
    else:
        total = subtotal
    return total