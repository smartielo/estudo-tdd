def depositar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor do depósito deve ser positivo.")
    novo_saldo = saldo + valor
    return novo_saldo

def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo.")
    if valor > saldo:
        raise ValueError("Saldo insuficiente para o saque.")
    novo_saldo = saldo - valor
    return novo_saldo

def calcular_rendimentos(saldo, meses):
    if meses < 0:
        raise ValueError("O número de meses não pode ser negativo.")
    taxa_juros_mensal = 0.01  # 1% ao mês
    rendimentos = saldo * taxa_juros_mensal * meses
    saldoNovo = saldo + rendimentos
    return saldoNovo