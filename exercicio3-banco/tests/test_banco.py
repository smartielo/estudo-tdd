from banco import depositar, sacar, calcular_rendimentos 
import pytest


def test_depositar():
    assert depositar(100, 50) == 150
    with pytest.raises(ValueError):
        depositar(100, -50)
    with pytest.raises(ValueError):
        depositar(100, 0)

def test_sacar():
    assert sacar(100, 50) == 50
    with pytest.raises(ValueError):
        sacar(100, 150)
    with pytest.raises(ValueError):
        sacar(100, 0)   

def test_calcular_rendimentos():
    assert calcular_rendimentos(1000, 12) == 1120
    with pytest.raises(ValueError):
        calcular_rendimentos(1000, -12)


