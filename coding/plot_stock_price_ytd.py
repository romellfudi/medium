# filename: plot_stock_price_ytd.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Replace 'STOCK_SYMBOL' with the actual stock symbol you want to plot
stock_symbol = 'STOCK_SYMBOL'

# Set the start date to the beginning of the current year
start_date = datetime(datetime.now().year, 1, 1)

# Download the stock data
data = yf.download(stock_symbol, start=start_date)

# Calculate the price change
data['Price Change'] = data['Adj Close'].pct_change()

# Plot the price change
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Price Change'], label='Price Change YTD')
plt.title(f'{stock_symbol} Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Price Change')
plt.legend()
plt.grid(True)

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')
plt.show()