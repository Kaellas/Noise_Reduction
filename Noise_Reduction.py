import pandas as pd
import os

# --- Reading Data ---

# Setting wd
os.chdir("/Users/pawelgach/Desktop/Noise_Reduction")

# Assuming data is in CSV files
data_1min = pd.read_csv('BacktestData_1min.csv', sep=";")
data_5min = pd.read_csv('BacktestData_5min.csv', sep=";")
data_15min = pd.read_csv('BacktestData_15min.csv', sep=";")

# Make sure Timestamp is a datetime object
data_1min['Timestamp'] = pd.to_datetime(data_1min['Timestamp'])
data_5min['Timestamp'] = pd.to_datetime(data_5min['Timestamp'])
data_15min['Timestamp'] = pd.to_datetime(data_15min['Timestamp'])


# Display the first few rows of each dataframe to verify
print(data_1min.head())
print(data_5min.head())
print(data_15min.head())

# --- Noise Reduction ---

# Create mid-price by taking average of the High and Low columns
data_1min['Mid'] = (data_1min['High'] + data_1min['Low']) / 2
data_5min['Mid'] = (data_5min['High'] + data_5min['Low']) / 2
data_15min['Mid'] = (data_15min['High'] + data_15min['Low']) / 2

# Verify
print(data_1min.head())
print(data_5min.head())
print(data_15min.head())

# Applying a moving average to smooth the data
data_1min['MA5'] = data_1min['Mid'].rolling(window=5).mean()
data_5min['MA5'] = data_5min['Mid'].rolling(window=5).mean()
data_15min['MA5'] = data_15min['Mid'].rolling(window=5).mean()

# Drop the first 4 rows for which price_smooth is empty
data_1min = data_1min.iloc[4:]
data_5min = data_5min.iloc[4:]
data_15min = data_15min.iloc[4:]

# Drop the Low, High, Open, Close and Volume columns
data_1min = data_1min.drop(columns=['Low', 'High', 'Open', 'Close', 'Volume'])
data_5min = data_5min.drop(columns=['Low', 'High', 'Open', 'Close', 'Volume'])
data_15min = data_15min.drop(columns=['Low', 'High', 'Open', 'Close', 'Volume'])

# Verify
print(data_1min.head())
print(data_5min.head())
print(data_15min.head())

# --- Basic Analysis ---

import numpy as np

# Calculate returns
data_1min['Return'] = data_1min['Mid'].pct_change()
data_5min['Return'] = data_5min['Mid'].pct_change()
data_15min['Return'] = data_15min['Mid'].pct_change()

# Display basic statistics
# Important:
# Volatility (standard deviation of Return)
# Average Return (mean of Return)
print('1-Minute Data Statistics:')
print(data_1min.describe())
print('\n5-Minute Data Statistics:')
print(data_5min.describe())
print('\n15-Minute Data Statistics:')
print(data_15min.describe())


# --- Plotting ---

import matplotlib.pyplot as plt

# Return Distributions
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot return distributions
axs[0].hist(data_1min['Return'], bins=50, alpha=0.6, label='1-Min', color="blue")
axs[0].set_title('1-Min Return Distribution')
axs[0].set_xlabel('Return')
axs[0].set_ylabel('Frequency')

axs[1].hist(data_5min['Return'], bins=50, alpha=0.6, label='5-Min', color="red")
axs[1].set_title('5-Min Return Distribution')
axs[1].set_xlabel('Return')
axs[1].set_ylabel('Frequency')

axs[2].hist(data_15min['Return'], bins=50, alpha=0.6, label='15-Min', color="green")
axs[2].set_title('15-Min Return Distribution')
axs[2].set_xlabel('Return')
axs[2].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()


# Volatility Clustering
fig, axs = plt.subplots(3, 1, figsize=(15, 15))

# 1-Min Plot
axs[0].scatter(data_1min['Timestamp'], data_1min['Return'], label='1-Min', alpha=0.7, s=1, c='black')
axs[0].set_title('1-Min Return')
axs[0].set_xlabel('Timestamp')
axs[0].set_ylabel('Return')
axs[0].tick_params(axis='x', rotation=45)
axs[0].xaxis.set_major_locator(plt.MaxNLocator(10))

# 5-Min Plot
axs[1].scatter(data_5min['Timestamp'], data_5min['Return'], label='5-Min', alpha=0.7, s=1, c='black')
axs[1].set_title('5-Min Return')
axs[1].set_xlabel('Timestamp')
axs[1].set_ylabel('Return')
axs[1].tick_params(axis='x', rotation=45)
axs[1].xaxis.set_major_locator(plt.MaxNLocator(10))

# 15-Min Plot
axs[2].scatter(data_15min['Timestamp'], data_15min['Return'], label='15-Min', alpha=0.7, s=1, c='black')
axs[2].set_title('15-Min Return')
axs[2].set_xlabel('Timestamp')
axs[2].set_ylabel('Return')
axs[2].tick_params(axis='x', rotation=45)
axs[2].xaxis.set_major_locator(plt.MaxNLocator(10))

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(hspace=1)  # Increase hspace value to add more vertical space

# Display the plots
plt.show()