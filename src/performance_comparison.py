import pandas as pd
import time


def comparar_com_pandas():
    """Compara o desempenho usando Pandas."""
    start_time = time.time()
    
    tesla_data = pd.read_csv('data/raw_data/tesla_prices.csv')
    
    # Converter para número e remover valores inválidos
    tesla_data['Close'] = pd.to_numeric(tesla_data['Close'], errors='coerce')
    
    # Remover linhas onde "Close" é NaN (caso existam)
    tesla_data = tesla_data.dropna(subset=['Close'])
    
    tesla_data['Media_Movel'] = tesla_data['Close'].rolling(window=7).mean()
    
    end_time = time.time()
    print(f"Tempo de execução com o Pandas: {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    comparar_com_pandas()
