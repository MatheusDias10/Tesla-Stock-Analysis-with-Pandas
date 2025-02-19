# src/data_download.py

import yfinance as yf
from pycoingecko import CoinGeckoAPI
import pandas as pd

def download_acao(acao):
    """Baixa os dados históricos de ações do yfinance."""
    df = yf.download(acao, period="6mo")
    return df

def download_cripto(cripto, moeda='usd'):
    cg = CoinGeckoAPI()
    dados_cripto = cg.get_coin_market_chart_by_id(id=cripto, vs_currency=moeda, from_timestamp=1609459200, to_timestamp=1672531200)
    df_cripto = pd.DataFrame(dados_cripto['prices'], columns=["Timestamp", "Preço"])
    df_cripto["Timestamp"] = pd.to_datetime(df_cripto["Timestamp"], unit="ms")
    return df_cripto

if __name__ == "__main__":
    # Baixar dados de ações e criptos
    acao = download_acao("TSLA")  # Corrigido para TSLA
    acao.to_csv("data/raw_data/tesla_prices.csv")  # Corrigido para o nome correto do arquivo
