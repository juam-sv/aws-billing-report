import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('costs.csv')

# Informações gerais do arquivo
print("Informações gerais:")
print(df.info())
print("\n")

# Visualizar as primeiras linhas do arquivo
print("Primeiras linhas do arquivo:")
print(df.head())
print("\n")

# Gráfico de barras para os valores totais por conta
df_total_costs = df[['Linked account name', 'Total costs ($)']]
df_total_costs = df_total_costs.iloc[2:].copy()  # Excluir as primeiras duas linhas com informações não relevantes

plt.figure(figsize=(12, 6))
plt.bar(df_total_costs['Linked account name'], df_total_costs['Total costs ($)'])
plt.xticks(rotation=90)
plt.xlabel('Conta vinculada')
plt.ylabel('Custo total ($)')
plt.title('Custos totais por conta vinculada')
plt.tight_layout()
plt.show()
