import pandas as pd
import os

def clean_data(input_file, output_file):
    # Tentar carregar o CSV sem cabeçalho para examinar os dados
    df = pd.read_csv(input_file, header=None)
    
    # Exibir as primeiras linhas para verificar como os dados estão estruturados
    print("Primeiras linhas com header=None:")
    print(df.head())
    
    # Exibir os nomes das colunas para verificar se estão desalinhadas
    print("Colunas do DataFrame:", df.columns.tolist())
    
    # Ajuste manual do cabeçalho: assumimos que a segunda linha (índice 1) é a correta
    df.columns = df.iloc[1]  # Atribui a segunda linha como nome das colunas
    df = df.drop([0, 1])  # Remove as duas primeiras linhas que agora são cabeçalhos
    
    # Limpar as colunas com valores NaN ou que não são úteis
    df = df.dropna(axis=1, how='all')  # Remove colunas totalmente vazias
    df.columns = df.columns.str.strip()  # Limpar possíveis espaços nos nomes das colunas
    
    # Verificar novamente os dados após ajustar as colunas
    print("Primeiras linhas após ajuste de cabeçalho:")
    print(df.head())
    
    # Exibir os nomes das colunas após o ajuste
    print("Colunas após o ajuste:", df.columns.tolist())
    
    # Verificar se a coluna 'Date' existe após ajuste
    if 'Date' not in df.columns:
        print("A coluna 'Date' não foi encontrada!")
        return
    
    # Exibir conteúdo da coluna "Date" para verificar sua leitura
    print("Conteúdo da coluna 'Date':")
    print(df['Date'].head())
    
    # Converter a coluna "Date" para datetime e remover linhas com valores inválidos
    df = df[pd.to_datetime(df["Date"], errors="coerce").notna()]
    
    # Exibir as primeiras linhas após limpeza
    print("Primeiras linhas após limpar a coluna 'Date':")
    print(df.head())
    
    # Verificar se o diretório de saída existe, se não, cria-lo
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Salvar o DataFrame limpo
    df.to_csv(output_file, index=False)
    print(f"Dados limpos salvos em {output_file}")

if __name__ == "__main__":
    input_file = "data/processed_data/tesla_processed.csv"  # Substitua com o caminho do seu arquivo CSV/input_file.csv"
    output_file = "data/cleaned_data/tesla_cleaned.csv"
    clean_data(input_file, output_file)
