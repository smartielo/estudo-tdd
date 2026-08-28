def calcular_media(notap1, notap2, notaoutros):
    if 0 <= notap1 <= 10 and 0 <= notap2 <= 10 and 0 <= notaoutros <= 10:
        return (notap1 + notap2) * 0.35 + notaoutros * 0.3
    raise ValueError("As notas devem estar entre 0 e 10.")


def verificar_situacao(calcular_media):
    if calcular_media >= 7:
        return "Aprovado"
    elif calcular_media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def maior_nota(notasp1, notasp2, notasoutros):
    if 0 <= notasp1 <= 10 and 0 <= notasp2 <= 10 and 0 <= notasoutros <= 10:
        return max(notasp1, notasp2, notasoutros)
    raise ValueError("As notas devem estar entre 0 e 10.")


def menor_nota(notasp1, notasp2, notasoutros):
    if 0 <= notasp1 <= 10 and 0 <= notasp2 <= 10 and 0 <= notasoutros <= 10:
        return min(notasp1, notasp2, notasoutros)
    raise ValueError("As notas devem estar entre 0 e 10.")