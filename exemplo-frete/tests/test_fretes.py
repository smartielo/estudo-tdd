import pytest
from run import calcular_frete


def test_peso_menor_que_zero():
    with pytest.raises(ValueError):
        calcular_frete(-2, 0) == 0