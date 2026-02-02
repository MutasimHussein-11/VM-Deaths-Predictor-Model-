# “Expected deaths per year ≈ historical average”

<<<<<<< HEAD
=======
# “Expected deaths over the next N years = average × N”

>>>>>>> 7e3432c143443cde6a908eda6225a6503f4e81cd
# Average: 2.18 deaths

# data -> model -> prediction

# Update
<<<<<<< HEAD
# start the prediction model
# “Expected deaths over the next N years = average × N”
=======
# show plot of vending data
>>>>>>> 7e3432c143443cde6a908eda6225a6503f4e81cd

from sklearn.datasets import fetch_california_housing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_excel('Stats.xlsx')
<<<<<<< HEAD
df2 = pd.read_excel('Stats2.xlsx')

# Make sure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y')
df2['Date'] = pd.to_datetime(df2['Date'], format='%Y')

plt.figure()
plt.plot(df['Date'], df.iloc[:, 1], marker='o')
plt.plot(df2['Date'], df2.iloc[:, 1], marker='o')
=======

# Make sure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y')

# Plot exactly what you want
plt.figure()
plt.plot(df['Date'], df.iloc[:, 1], marker='o')
>>>>>>> 7e3432c143443cde6a908eda6225a6503f4e81cd

plt.xlabel('Year')
plt.ylabel('Value')

# Format x-axis to show years only
ax = plt.gca()
<<<<<<< HEAD
ax.xaxis.set_major_locator(mdates.YearLocator(5))
=======
ax.xaxis.set_major_locator(mdates.YearLocator())
>>>>>>> 7e3432c143443cde6a908eda6225a6503f4e81cd
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.tight_layout()
plt.show()
