from aluguel import calcular_diarias, adicionar_seguro, fechar_aluguel
import pytest

def test_calcular_diarias():
    assert calcular_diarias(3, "Economico") == 300
    assert calcular_diarias(2, "Sedan") == 300
    assert calcular_diarias(1, "SUV") == 200
    with pytest.raises(ValueError):
        calcular_diarias(0, "Economico")
    with pytest.raises(ValueError):
        calcular_diarias(3, "Luxo")

def test_adicionar_seguro():
    assert adicionar_seguro(100, "Basico") == 150
    assert adicionar_seguro(100, "Premium") == 250
    with pytest.raises(ValueError):
        adicionar_seguro(100, "Standard")

def test_fechar_aluguel():
    assert fechar_aluguel(3, "Economico") == 300
    assert fechar_aluguel(2, "Sedan") == 300
    assert fechar_aluguel(1, "SUV") == 200
    assert fechar_aluguel(3, "Economico", "Basico") == 350
    assert fechar_aluguel(2, "Sedan", "Premium") == 450