# Mini-projeto-completo-Pandas-Matplotlib
Mini-projeto completo Pandas + Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Criando dataset fictício
data = {
    "Aluno": ["Aluno " + str(i) for i in range(1, 21)],
    "Altura(cm)": [160, 165, 170, 158, 175, 168, 162, 171, 169, 166,
                   173, 164, 172, 167, 159, 174, 161, 170, 168, 165],
    "Peso(kg)": [55, 60, 68, 52, 75, 63, 57, 70, 66, 61,
                 72, 59, 71, 64, 53, 73, 56, 69, 65, 60]
}

df = pd.DataFrame(data)

# 2️⃣ Exploração básica
print("Primeiras linhas:\n", df.head())
print("\nInformações gerais:\n", df.info())
print("\nEstatísticas descritivas:\n", df.describe())

# 3️⃣ Estatísticas principais
altura_media = df["Altura(cm)"].mean()
peso_medio = df["Peso(kg)"].mean()
print("\nAltura média:", altura_media)
print("Peso médio:", peso_medio)

# 4️⃣ Adicionando coluna de IMC
df["IMC"] = df["Peso(kg)"] / ((df["Altura(cm)"]/100) ** 2)
print("\nDataset com IMC:\n", df)

# 5️⃣ Identificando alunos acima da média
acima_media = df[(df["Altura(cm)"] > altura_media) & (df["Peso(kg)"] > peso_medio)]
print("\nAlunos acima da média em altura e peso:\n", acima_media)

# 6️⃣ Gráficos

# 6.1 Histograma de alturas
plt.hist(df["Altura(cm)"], bins=5, color="skyblue", edgecolor="black")
plt.title("Distribuição de Alturas")
plt.xlabel("Altura (cm)")
plt.ylabel("Número de alunos")
plt.show()

# 6.2 Histograma de pesos
plt.hist(df["Peso(kg)"], bins=5, color="lightgreen", edgecolor="black")
plt.title("Distribuição de Pesos")
plt.xlabel("Peso (kg)")
plt.ylabel("Número de alunos")
plt.show()

# 6.3 Gráfico de dispersão Altura x Peso com IMC colorido
plt.scatter(df["Altura(cm)"], df["Peso(kg)"], c=df["IMC"], cmap="coolwarm", s=100)
plt.colorbar(label="IMC")
plt.title("Altura x Peso (colorido por IMC)")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.show()

# 6.4 Gráfico de barras do peso por aluno
plt.bar(df["Aluno"], df["Peso(kg)"], color="purple")
plt.title("Peso de cada aluno")
plt.xlabel("Aluno")
plt.ylabel("Peso (kg)")
plt.xticks(rotation=45)
plt.show()
