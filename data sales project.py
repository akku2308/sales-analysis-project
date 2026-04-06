# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:39:55 2026

@author: ashis
"""

import pandas as pd 
data = pd.read_csv("C:/Users/ashis/Downloads/AKKU/train.csv")
print(data.head())

print(data.head(15))
print(data.columns)
print(data.shape)
print(data.info())
print(data.isnull().sum())
print(data.dropna())
print(data['Sales'].sum())
print(data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10))
data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).plot(kind='bar')
import matplotlib.pyplot as plt
data.groupby('Category')['Sales'].sum().plot(kind='bar')
plt.show()


import matplotlib.pyplot as plt
data['Order Date'] = pd.to_datetime(data['Order Date'],format='mixed')
data.groupby('Order Date')['Sales'].sum().plot(kind='bar')
plt.show()

data.groupby(data['Order Date'].dt.to_period('M'))['Sales'].sum().plot(kind='bar')
plt.show()

data.groupby(data['Order Date'].dt.to_period('Y'))['Sales'].sum().plot(kind='bar')
plt.show()

