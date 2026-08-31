
notas = []

def calcular_media(notas):
    if len(notas) != 3:
        raise ValueError("Devem ser fornecidas exatamente 3 notas.")
    if 0 <= notas[0] <= 10 and 0 <= notas[1] <= 10 and 0 <= notas[2] <= 10:
        return round(((notas[0] + notas[1]) * 0.35 + notas[2] * 0.3), 2)
    raise ValueError("As notas devem estar entre 0 e 10.")


def verificar_situacao(calcular_media):
    if calcular_media >= 7:
        return "Aprovado"
    elif calcular_media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def maior_nota(notas):
    if 0 <= notas[0] <= 10 and 0 <= notas[1] <= 10 and 0 <= notas[2] <= 10:
        return max(notas)
    raise ValueError("As notas devem estar entre 0 e 10.")


def menor_nota(notas):
    if 0 <= notas[0] <= 10 and 0 <= notas[1] <= 10 and 0 <= notas[2] <= 10:
        return min(notas)
    raise ValueError("As notas devem estar entre 0 e 10.")