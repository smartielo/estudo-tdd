import pytest
from loja import calcular_subtotal, aplicar_cupom, calcular_compra



def test_calcular_compra():
    assert calcular_compra([10]) == 10
    assert calcular_compra([10], "DESC10") == 9.0
    assert calcular_compra([10, 10, 10], "DESC20") == 24.0
    assert calcular_compra([10, 10, 10], "SEMANA30") == 21.0
    with pytest.raises(ValueError):
        calcular_compra([], "DESC10")
    with pytest.raises(ValueError):
        calcular_compra([10, 10, 10], "CUPOMFAKE")


def test_calcular_subtotal():
    assert calcular_subtotal([10]) == 10
    assert calcular_subtotal([10, 20, 30]) == 60
    with pytest.raises(ValueError):
        calcular_subtotal([])
    with pytest.raises(ValueError):
        calcular_subtotal([-10, 20, 30])
    with pytest.raises(ValueError):
        calcular_subtotal([10, -20, 30])
    with pytest.raises(ValueError):
        calcular_subtotal([10, 20, -30])
    with pytest.raises(ValueError):
        calcular_subtotal([0, 20, 30])
    with pytest.raises(ValueError):
        calcular_subtotal([10, 0, 30])
    with pytest.raises(ValueError):
        calcular_subtotal([10, 20, 0])
    