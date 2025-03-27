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

# V2: Bar chart of average PM 2.5 by Geo Place Name
pm25_data = data[data['Indicator ID'] == 365]
average_pm25 = pm25_data.groupby('Geo Place Name')['Data Value'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 8))
average_pm25.plot(kind='bar', color='green')
plt.title('Average PM 2.5 Levels by Geo Place Name')
plt.xlabel('Geo Place Name')
plt.ylabel('Average PM 2.5 Level (mcg/m3)')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


# V3: Line plot of NO2 levels over time for a specific place
flushing_data = data[(data['Geo Place Name'] == 'Flushing and Whitestone (CD7)') & (data['Indicator ID'] == 375)]
flushing_data = flushing_data.sort_values('Start_Date')

plt.figure(figsize=(12, 6))
plt.plot(flushing_data['Start_Date'], flushing_data['Data Value'], marker='o', linestyle='-', color='red')
plt.title('NO2 Levels Over Time in Flushing and Whitestone (CD7)')
plt.xlabel('Date')
plt.ylabel('NO2 Level (ppb)')
plt.grid(True)
plt.show()