# filename: plot_invented_stock_price_ytd.py
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Generate a date range from the start of the current year to today
start_date = datetime(datetime.now().year, 1, 1)
end_date = datetime.now()
date_range = pd.date_range(start_date, end_date)

# Invent stock price data with random walk
np.random.seed(0)  # For reproducibility
price_changes = np.random.randn(len(date_range))  # Daily price changes
prices = 100 + np.cumsum(price_changes)  # Starting price of 100

# Create a DataFrame with the invented stock price data
data = pd.DataFrame(data={'Date': date_range, 'Price': prices})
data.set_index('Date', inplace=True)

# Calculate the daily price change percentage
data['Price Change'] = data['Price'].pct_change()

# Plot the price change
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Price Change'], label='Price Change YTD', color='blue')
plt.title('Invented Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Price Change (%)')
plt.legend()
plt.grid(True)

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')
plt.show()