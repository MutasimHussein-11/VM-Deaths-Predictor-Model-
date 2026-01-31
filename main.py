# “Expected deaths per year ≈ historical average”

# “Expected deaths over the next N years = average × N”

# Average: 2.18 deaths

# data -> model -> prediction

# Update
# show plot of vending data

from sklearn.datasets import fetch_california_housing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_excel('Stats.xlsx')

# Make sure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y')

# Plot exactly what you want
plt.figure()
plt.plot(df['Date'], df.iloc[:, 1], marker='o')

plt.xlabel('Year')
plt.ylabel('Value')

# Format x-axis to show years only
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.tight_layout()
plt.show()
