import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def optimal_number_of_clusters(file_name, sheet_name, max_clusters=10):
    # Ler o arquivo Excel e a planilha especificada
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    
    # Selecionar as colunas independentes para clustering
    features = ['Potência do Veículo', 'Idade do Veículo', 'IPVA']
    
    data = df[features]
    
    # Normalizar os dados
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    # Calcular a soma das distâncias quadráticas intra-cluster (inertia) para diferentes valores de k
    inertia = []
    k_range = range(1, max_clusters + 1)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data_scaled)
        inertia.append(kmeans.inertia_)
    
    # Encontrar o "cotovelo" no gráfico (onde a redução de inertia começa a se estabilizar)
    # Usar a segunda derivada da inertia para identificar o ponto de inflexão
    deltas = np.diff(inertia)
    second_deltas = np.diff(deltas)
    optimal_k = np.argmax(second_deltas) + 2  # +2 porque a primeira diff reduz o índice em 1 e a segunda diff reduz em outro 1
    
    return optimal_k

def kmeans_clustering(file_name, sheet_name, n_clusters=3):
    # Ler o arquivo Excel e a planilha especificada
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    
    # Selecionar as colunas independentes para clustering
    features = ['Potência do Veículo', 'Idade do Veículo', 'IPVA']
    data = df[features]
    
    # Normalizar os dados
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    # Aplicar K-means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data_scaled)
    
    # Adicionar os rótulos dos clusters ao dataframe original
    df['Cluster'] = kmeans.labels_
    
    # Salvar o resultado em um novo arquivo Excel
    output_file_name = 'kmeans_output.xlsx'
    df.to_excel(output_file_name, index=False)
    print(f'Resultados salvos no arquivo: {output_file_name}')

    return df, kmeans

# Exemplo de uso
file_name = 'planilhaFinal.xlsx'
sheet_name = 'NovaAmostra'
n_clusters = optimal_number_of_clusters(file_name, sheet_name)
#n_clusters = 4
print(f'Número ótimo de clusters: {n_clusters}')

df_result, kmeans_model = kmeans_clustering(file_name, sheet_name, n_clusters)

# Plot 3D para visualização (opcional)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Defina as colunas que deseja usar para o gráfico 3D
x_column = 'Potência do Veículo'
y_column = 'Idade do Veículo'
z_column = 'IPVA'

x = df_result[x_column]
y = df_result[y_column]
z = df_result[z_column]
clusters = df_result['Cluster']

scatter = ax.scatter(x, y, z, c=clusters, cmap='viridis')
ax.set_title('K-means Clustering 3D')
ax.set_xlabel(x_column)
ax.set_ylabel(y_column)
ax.set_zlabel(z_column)

# Adiciona a legenda
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)

plt.show()
