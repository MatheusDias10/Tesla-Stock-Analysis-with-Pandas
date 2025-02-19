import pandas as pd
import matplotlib.pyplot as plt

def plotar_acao(df):
    """Cria um gráfico da ação com média móvel e preço de fechamento."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Close'], label="Preço Fechamento")
    plt.plot(df['Date'], df['Media_Movel'], label="Média Móvel (7 dias)", linestyle='--', color='orange')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.title('Preço de Fechamento e Média Móvel')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Carregar o CSV ignorando a primeira linha e sem gerar mensagens
    tesla_data = pd.read_csv("data/processed_data/tesla_processed.csv", header=2, parse_dates=['Date'])
    
    # Renomear as colunas de forma explícita
    tesla_data.columns = ['Date', 'Price', 'Close', 'High', 'Low', 'Open', 'Volume', 'Media_Movel', 'Variação_Percentual']

    print(tesla_data.head())
    plotar_acao(tesla_data)
