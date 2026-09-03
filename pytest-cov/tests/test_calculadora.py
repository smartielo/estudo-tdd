from calculadora import somar, subtrair, multiplicar, dividir
import pytest

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(-1, 1) == -2
    assert subtrair(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 0) == 0

def test_dividir():
    assert dividir(6, 2) == 3
    assert dividir(-6, 2) == -3
    assert dividir(0, 1) == 0

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(1, 0)