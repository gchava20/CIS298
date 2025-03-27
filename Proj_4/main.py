import pandas as pd
import matplotlib as plt
import csv

data = pd.read_csv('Air_Quality.csv')
print(data.isnull().sum())

data = data.dropna(subset=['Data Value'])

