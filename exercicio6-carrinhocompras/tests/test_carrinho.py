from carrinho import calcular_total_item, calcular_total_carrinho
import pytest

def test_calcular_total_item():
    assert calcular_total_item(50, 2) == 100
    with pytest.raises(ValueError, match=r"Preço e Quantidade devem ser maiores que zero."):
        calcular_total_item(50, 0)
    with pytest.raises(ValueError, match=r"Preço e Quantidade devem ser maiores que zero."):
        calcular_total_item(-10, 2)

def test_calcular_total_carrinho():
    carrinho_exemplo = [
        {"preco": 50, "quantidade": 2},
        {"preco": 30, "quantidade": 1}
    ]
    
    assert calcular_total_carrinho(carrinho_exemplo) == 130


def test_calcular_total_carrinho_com_desconto():
    carrinho_exemplo = [
        {"preco": 100, "quantidade": 1},
        {"preco": 100, "quantidade": 1},
        {"preco": 100, "quantidade": 1}
    ]
    assert calcular_total_carrinho(carrinho_exemplo) == 270