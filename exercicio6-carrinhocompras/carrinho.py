def calcular_total_item(preco, quantidade):
    if(preco > 0 and quantidade > 0):
        totalItem = preco * quantidade
    else:
        raise ValueError("Preço e Quantidade devem ser maiores que zero.")
    return totalItem

def calcular_total_carrinho(carrinho):
    totalCarrinho = 0
    for i in carrinho:
        valorItem = i["preco"] * i["quantidade"]
        totalCarrinho += valorItem
    if totalCarrinho >= 200:
        valorDesconto = totalCarrinho * 10 / 100
        totalCarrinho -= valorDesconto
    return totalCarrinho