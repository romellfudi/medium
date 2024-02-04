# filename: plot_stock_price.py

import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

# Define the stock to be plotted
stock = 'YOUR_STOCK_TICKER'

# Define the date range
end_date = datetime.date.today()
start_date = datetime.date(end_date.year, 1, 1)

# Fetch the data
df = pdr.get_data_yahoo(stock, start_date, end_date)

# Plot the adjusted close price
df['Adj Close'].plot(grid=True)

# Set the title and labels
plt.title(f'{stock} Stock Price YTD')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')