import json

def calcular_faturamento(faturamento_diario):
    # Calcular menor e maior faturamento
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    
    # Calcular a média mensal
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    
    # Contar os dias em que o faturamento diário foi superior à média
    dias_superior_media = sum(1 for fat in faturamento_diario if fat > media_mensal)

    return menor_faturamento, maior_faturamento, dias_superior_media

# Caminho do arquivo JSON
caminho_arquivo = r"C:\Users\D.K\Desktop\Curso Dio.Pro\Desafio target\dados.json"

# Carrega os dados do arquivo JSON
with open(caminho_arquivo, 'r') as arquivo:
    dados_faturamento = json.load(arquivo)

# Extrai os valores de faturamento
faturamento_diario = [dado['valor'] for dado in dados_faturamento]

# Chama a função e obtém os resultados
menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

# Exibe os resultados
print(f"Menor faturamento do mês: R$ {menor:.2f}")
print(f"Maior faturamento do mês: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
