from carrinho import calcular_total_item
import pytest


def test_calcular_total_item():
    assert calcular_total_item(50, 2) == 100
    with pytest.raises(ValueError, match=r"Preço e Quantidade devem ser maiores que zero."):
        calcular_total_item(50, 0)
    with pytest.raises(ValueError, match=r"Preço e Quantidade devem ser maiores que zero."):
        calcular_total_item(-10, 2)