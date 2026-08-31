def calcular_diarias(dias, categoria):
    subtotal = 0
    if dias <= 0:
        raise ValueError("A quantidade de dias deve ser maior que zero.")
    if categoria == "Economico":
        subtotal = dias * 100
    elif categoria == "Sedan":
        subtotal = dias * 150
    elif categoria == "SUV":
        subtotal = dias * 200
    else:
        raise ValueError("A categoria informada não existe.")
    return subtotal

def adicionar_seguro(valor, tipo_seguro):
    if valor <= 0:
        raise ValueError("O valor tem que ser positivo.")
    if tipo_seguro == "Basico":
        novoValor = valor + 50
    elif tipo_seguro == "Premium":
        novoValor = valor + 150
    else:
        raise ValueError("O seguro informado não existe.")
    return novoValor

def fechar_aluguel (dias, categoria, tipo_seguro=None):
    subtotal = calcular_diarias(dias, categoria)
    total = subtotal
    if tipo_seguro != None:
        total = adicionar_seguro(subtotal, tipo_seguro)
    return total