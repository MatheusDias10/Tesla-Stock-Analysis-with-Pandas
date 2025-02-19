import pandas as pd

def calcular_media_movel(df, window=7):
    """Calcula a média móvel de 7 dias."""
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')  # Força a conversão para numérico
    df['Media_Movel'] = df['Close'].rolling(window=window).mean()
    return df

def calcular_variacao_percentual(df):
    """Calcula a variação percentual entre os preços de fechamento."""
    df['Variação_Percentual'] = df['Close'].pct_change() * 100
    return df

if __name__ == '__main__':
    # Carregar e processar dados
    tesla_data = pd.read_csv('data/raw_data/tesla_prices.csv')
    tesla_data = calcular_media_movel(tesla_data)
    tesla_data = calcular_variacao_percentual(tesla_data)

    tesla_data.to_csv('data/processed_data/tesla_processed.csv')
