from cinema import calcular_ingresso, comprar_lanche, fechar_pedido
import pytest

def test_calcular_ingresso_crianca():
    with pytest.raises(ValueError):
        calcular_ingresso(-1, False)
    with pytest.raises(ValueError):
        calcular_ingresso(0, False)
    assert calcular_ingresso(10, False) == 15
    assert calcular_ingresso(30, True) == 15 
    assert calcular_ingresso(65, False) == 15
    assert calcular_ingresso(30, False) == 30


def test_comprar_lanche():
    assert comprar_lanche("Pipoca") == 20
    assert comprar_lanche("Refrigerante") == 10
    assert comprar_lanche("Combo") == 25
    with pytest.raises(ValueError):
        comprar_lanche("Chocolate")
    with pytest.raises(ValueError):
        comprar_lanche("")