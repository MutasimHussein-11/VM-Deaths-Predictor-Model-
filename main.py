# “Expected deaths per year ≈ historical average”

# Average: 2.18 deaths

# data -> model -> prediction

# Update
# start the prediction model
# “Expected deaths over the next N years = average × N”

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.dates as mdates

# load data
df = pd.read_excel('Stats.xlsx')

# convert date to int
df['Year'] = df['Date'].astype(int)
X = df[['Year']]  # X
y = df.iloc[:, 1]  # Y

# linear regression
model = LinearRegression()
model.fit(X, y)

df['Predicted'] = model.predict(X)

# 10 years
last_year = df['Year'].max()
future_years = np.arange(last_year + 1, last_year + 11).reshape(-1, 1)
future_preds = model.predict(future_years)

# prepare future dataframe
future_df = pd.DataFrame({
    'Year': future_years.flatten(),
    'Predicted': future_preds
})

# plotting
plt.figure(figsize=(10,6))
plt.plot(df['Year'], df.iloc[:, 1], marker='o', label='Actual')
plt.plot(future_df['Year'], future_df['Predicted'], marker='x', linestyle=':', color='red', label='Future Predictions')

plt.xlabel('Year')
plt.ylabel('Value')

plt.title('Vending Machine Death Linear Regression Predictions')
plt.legend()

plt.grid(True)
plt.show()
