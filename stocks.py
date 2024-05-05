
import yfinance as yf
import numpy as np
import pandas as pd

# Import the price data of General Motors

df = yf.download('AAPL','2001-01-02', '2020-10-31')
df.to_csv(r'Stocks_dataset.csv')
