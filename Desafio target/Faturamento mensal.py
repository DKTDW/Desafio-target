# Faturamento mensal detalhado por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total
total_faturamento = sum(faturamento.values())

# Calcula e exibe a porcentagem de representação de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f'{estado}: {percentual:.2f}%')
