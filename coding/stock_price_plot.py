# filename: stock_price_plot.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generate sample stock price data for YTD (250 trading days)
np.random.seed(0)  # For reproducibility
dates = pd.date_range(start='2023-01-01', periods=250, freq='B')  # Business days in YTD
prices = np.random.normal(loc=100, scale=10, size=len(dates)).cumsum()  # Simulated stock prices

# Create a pandas DataFrame
data = pd.DataFrame({'Date': dates, 'Price': prices})
data.set_index('Date', inplace=True)

# Plot the stock price data
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Price'], label='Stock Price')
plt.title('Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Perform time series decomposition
decomposition = seasonal_decompose(data['Price'], model='additive', period=5)  # Weekly seasonality

# Plot the decomposition
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10))
decomposition.trend.plot(ax=ax1)
ax1.set_title('Trend')
ax1.grid(True)
decomposition.seasonal.plot(ax=ax2)
ax2.set_title('Seasonality')
ax2.grid(True)
decomposition.resid.plot(ax=ax3)
ax3.set_title('Residuals')
ax3.grid(True)

# Save the plots into a PNG file
plt.tight_layout()
plt.savefig('stock_price_ytd.png')

print("The stock price YTD chart and decomposition plots have been saved as 'stock_price_ytd.png'.")