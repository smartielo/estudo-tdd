import pytest
from run import calcular_media, maior_nota, menor_nota, verificar_situacao


def test_calcular_media():
    assert calcular_media(8, 7, 6) == 7.05
    assert calcular_media(10, 10, 10) == 10.0
    assert calcular_media(0, 0, 0) == 0.0
    with pytest.raises(ValueError):
        calcular_media(-1, 5, 5)
    with pytest.raises(ValueError):
        calcular_media(5, -1, 5)
    with pytest.raises(ValueError):
        calcular_media(5, 5, -1)
    with pytest.raises(ValueError):
        calcular_media(11, 5, 5)
    with pytest.raises(ValueError):
        calcular_media(5, 11, 5)
    with pytest.raises(ValueError):
        calcular_media(5, 5, 11)

def test_verificar_situacao():
    assert verificar_situacao(8) == "Aprovado"
    assert verificar_situacao(6) == "Recuperação"
    assert verificar_situacao(4) == "Reprovado"

def test_maior_nota():
    assert maior_nota(8, 7, 6) == 8
    assert maior_nota(10, 10, 10) == 10
    assert maior_nota(0, 0, 0) == 0
    with pytest.raises(ValueError):
        maior_nota(-1, 5, 5)
    with pytest.raises(ValueError):
        maior_nota(5, -1, 5)
    with pytest.raises(ValueError):
        maior_nota(5, 5, -1)
    with pytest.raises(ValueError):
        maior_nota(11, 5, 5)
    with pytest.raises(ValueError):
        maior_nota(5, 11, 5)
    with pytest.raises(ValueError):
        maior_nota(5, 5, 11)


def test_menor_nota():
    assert menor_nota(8, 7, 6) == 6
    assert menor_nota(10, 10, 10) == 10
    assert menor_nota(0, 0, 0) == 0
    with pytest.raises(ValueError):
        menor_nota(-1, 5, 5)
    with pytest.raises(ValueError):
        menor_nota(5, -1, 5)
    with pytest.raises(ValueError):
        menor_nota(5, 5, -1)
    with pytest.raises(ValueError):
        menor_nota(11, 5, 5)
    with pytest.raises(ValueError):
        menor_nota(5, 11, 5)
    with pytest.raises(ValueError):
        menor_nota(5, 5, 11)