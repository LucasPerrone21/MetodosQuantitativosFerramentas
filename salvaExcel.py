import pandas as pd

def salvaExcel(dados):
    nome_arquivo = "geral.xlsx"
    try:
        # Tentar ler os dados existentes do arquivo Excel, se existirem
        df_existente = pd.read_excel(nome_arquivo)
    except FileNotFoundError:
        # Se o arquivo não existir, criar um DataFrame vazio
        df_existente = pd.DataFrame()

    # Criar um DataFrame a partir dos novos dados
    df_novos = pd.DataFrame(dados)
    
    # Concatenar os dados existentes com os novos dados
    df_completo = pd.concat([df_existente, df_novos], ignore_index=True)
    
    # Salvar o DataFrame completo em um arquivo Excel
    df_completo.to_excel(nome_arquivo, index=False)