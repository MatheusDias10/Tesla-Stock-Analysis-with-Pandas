# Financial Market Data Analysis Project

This project involves extracting, processing, and analyzing financial market data, such as stock prices, using Python. The main goal is to compare the performance of different data processing tools, namely Pandas and Selenium, and visualize the trends in stock data. 

## Project Overview

- **Data Extraction**: Financial data is fetched using Selenium for web scraping, or through APIs such as Yahoo Finance, Alpha Vantage, or CoinGecko. Data includes stock prices, volume, and other relevant financial metrics.
  
- **Data Processing**: The extracted data is processed using Pandas for analysis. The focus is on calculating key metrics such as moving averages, price changes, and percentage variations over time.
  
- **Visualization**: Matplotlib is used to create visual representations of stock price trends and key metrics, allowing for deeper insights into market movements.
  
- **Performance Comparison**: A key part of this project is comparing the performance of Pandas with other potential tools for data processing, aiming to measure execution time and memory usage.

## Technologies Used

- **Pandas**: Data manipulation and analysis.
- **Selenium**: Web scraping for financial data extraction.
- **Matplotlib**: Data visualization.
- **Yahoo Finance, Alpha Vantage, CoinGecko**: Data sources (API/web scraping).
  
## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/MatheusDias10/tesla-stock-analysis-with-pandas.git
```
2. Navigate to the project directory:

```bash
cd tesla-stock-analysis-with-pandas
```
3. Install the dependencies:

```bash
pip install -r requirements.txt
```
Run the script to start the data analysis:

```bash
python src/data_analysis.py
```
