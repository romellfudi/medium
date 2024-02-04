# filename: plot_decomposed_stock_price_ytd.py
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

# Generate a date range from the start of the current year to today
start_date = datetime(datetime.now().year, 1, 1)
end_date = datetime.now()
date_range = pd.date_range(start_date, end_date)

# Invent stock price data with a random walk and a trend
np.random.seed(0)  # For reproducibility
price_changes = np.random.randn(len(date_range))  # Daily price changes
trend = np.linspace(0, 10, len(date_range))  # Linear trend
prices = 100 + np.cumsum(price_changes) + trend  # Starting price of 100 with trend

# Create a DataFrame with the invented stock price data
data = pd.DataFrame(data={'Price': prices}, index=date_range)

# Decompose the time series into trend, seasonal, and residual components
decomposition = seasonal_decompose(data['Price'], model='additive', period=30)

# Plot the original data, trend, seasonal, and residual components
plt.figure(figsize=(10, 8))

plt.subplot(411)
plt.plot(data, label='Original')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(decomposition.trend, label='Trend')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonality')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(decomposition.resid, label='Residuals')
plt.legend(loc='upper left')

# Adjust layout
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')
plt.show()