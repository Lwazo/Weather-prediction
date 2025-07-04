# -*- coding: utf-8 -*-
"""weather prediction Machine Learning .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11gd5r9zojagK1m4cKVnJtCpwyLS4k_88

##Weather Prediction with Linear Regression
"""

#import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

#loading a dataset
df = pd.read_csv('/content/weatherHistory.csv')

#preview the data
print(df.head())
print(df.info)

#selecting feartures and target
features = ['Humidity', 'Wind Speed (km/h)', 'Pressure (millibars)']
target = 'Temperature (C)'

x = df[features]
y = df[target]

#Training test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Training the Model
model = LinearRegression()
model.fit(x_train, y_train)

#Making predictions
y_pred = model.predict(x_test)

#Evaluating the model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Erro: ", round(mae, 2))
print("Root Mean Squared Error: ", round(rmse, 2))
print("R^2 Score: ", round(r2, 2))

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred, color='blue')
plt.xlabel('Actual Temperature')
plt.ylabel('Predicted Temperature')
plt.title('Actual vs Predicted Temperature')
plt.grid(True)
plt.show()