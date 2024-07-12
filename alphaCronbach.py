import pandas as pd
import numpy as np

def cronbach_alpha_standardized(items_scores):
    """
    Calcular o alpha de Cronbach padronizado.
    :param items_scores: DataFrame onde cada coluna representa um item.
    :return: Valor do alpha de Cronbach padronizado.
    """
    # Padronizar os itens
    standardized_items = (items_scores - items_scores.mean()) / items_scores.std(ddof=1)
    
    n_items = standardized_items.shape[1]
    item_variances = standardized_items.var(axis=0, ddof=1)
    total_variance = standardized_items.sum(axis=1).var(ddof=1)
    
    cronbach_alpha_value = (n_items / (n_items - 1)) * (1 - (item_variances.sum() / total_variance))
    return cronbach_alpha_value

# Carregar o arquivo Excel
file_path = 'planilhaFinal.xlsx'  # Substitua pelo caminho do seu arquivo
sheet_name = 'Planilha1'  # Substitua pelo nome da planilha

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Definir os grupos de colunas diretamente no código


# Definir os grupos de colunas diretamente no código
grupos = {
    'Grupo 1': ['Valor', 'Potência do Veículo', 'Idade do veículo', 'IPVA'],
}

# Calcula o alpha de Cronbach para cada grupo de colunas
cronbach_alphas = {}
for grupo, colunas in grupos.items():
    # Verifica se todas as colunas do grupo estão presentes no DataFrame
    if all(col in df.columns for col in colunas):
        cronbach_alphas[grupo] = cronbach_alpha_standardized(df[colunas])
    else:
        print(f'Algumas colunas do {grupo} não estão presentes na planilha.')

# Exibe os resultados
for grupo, alpha in cronbach_alphas.items():
    print(f'Alfa de Cronbach para {grupo}: {alpha:.4f}')
