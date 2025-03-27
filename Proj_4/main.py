import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir('/Users/gayathrichava/Documents/GitHub/CIS298/Proj_4/')

data = pd.read_csv('/Users/gayathrichava/Documents/GitHub/CIS298/Proj_4/Air_Quality.csv')
print(data.isnull().sum())

#drop rows where values are missing
data = data.dropna(subset=['Data Value'])

# V1: Histogram of NO2 levels
plt.figure(figsize=(10, 5))
plt.hist(data[data['Indicator ID'] == 375]['Data Value'], bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Nitrogen dioxide (NO2) Levels')
plt.xlabel('NO2 Level (ppb)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
