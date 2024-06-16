#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
# Sample DataFrame
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Revenue': [50000, 60000, 55000, 70000, 90000],
    'Expenses': [35000, 40000, 45000, 50000, 60000]
}

df = pd.DataFrame(data)
# Bar chart
plt.figure(figsize=(10, 6))

# Plotting bars
plt.bar(df['Year'], df['Revenue'], color='b', alpha=0.7, label='Revenue')
plt.bar(df['Year'], df['Expenses'], color='r', alpha=0.7, label='Expenses')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Revenue and Expenses Over Years')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
# Line chart
plt.figure(figsize=(10, 6))

# Plotting line
plt.plot(df['Year'], df['Revenue'], marker='o', linestyle='-', color='b', label='Revenue')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Revenue ($)')
plt.title('Revenue Trend Over Years')
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()

