def calcular_frete (peso, distancia, tipo="normal"):
    if peso <= 0:
        raise ValueError('O peso não pode ser menor que zero.')