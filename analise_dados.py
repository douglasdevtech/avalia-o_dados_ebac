import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/Users/DOUGL/Downloads/ecommerce-preparados.csv')
print(df.head().to_string())

# Tratamento de dados
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')  # Transformar a coluna em númerico
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].fillna(0)  # Substituir NaN por 0 (zero)
df['Marca'] = df['Marca'].astype('category').cat.codes  # Converte marcas para códigos


# Histograma
plt.hist(df['Qtd_Vendidos'])
plt.show()

# Gráfico de Dispersão
plt.scatter(df['Marca'], df['Qtd_Vendidos'])
plt.xlabel('Marca')
plt.ylabel('Qtd_Vendidos')
plt.title('Dispersão de Marca e Qtd_Vendida')
plt.show()

# Mapa de Calor
corr = df[['Marca', 'Qtd_Vendidos']].corr()
plt.subplot(2, 2, 3)  # 1 Linha, 2 Colunas, 3º Gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Relação Marca e Quantidade de Vendas')
plt.show()

# Gráfico de barra
plt.figure(figsize=(10, 6))
top_marcas = df['Marca'].value_counts().head(5).sort_values(ascending=True)
df['N_Avaliações'].value_counts().head(5).plot(kind='barh', color='#fcba03')
plt.title('Marca e Total de Avaliações')
plt.xlabel('Total de Avaliações', fontsize=10, labelpad=10)
plt.ylabel('Marcas', fontsize=10, labelpad=10)
plt.xticks(rotation=0)
plt.show()  # Exibe o Gráfico

# Gráfico de pizza
x = df['N_Avaliações'].value_counts().head(5).index
y = df['N_Avaliações'].value_counts().head(5).values

plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Marcas com maior porcentagem de Comentários')

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Qtd_Vendidos'], fill=True, color='#863e9c')
plt.title('Densidade de Qtd vendida')
plt.xlabel('Marca')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Marca', y='Qtd_Vendidos', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Qtd vendida por Marca')
plt.xlabel('Marca')
plt.ylabel('Qtd_Vendidos')
plt.show()