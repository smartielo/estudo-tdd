def calcular_total_item(preco, quantidade):
    if(preco > 0 and quantidade > 0):
        totalItem = preco * quantidade
    else:
        raise ValueError("Preço e Quantidade devem ser maiores que zero.")
    return totalItem

