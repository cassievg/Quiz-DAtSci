from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/nnqomariyah/Fundamentals_of_Data_Science/refs/heads/main/Dataset/healthcare_dataset_B.csv')

df['Age'].hist()
df['Name'].apply(lambda x: x.lower())
print(df.isnull().sum())
old = df.query('Age >= 80 and Medical Condition == "Arthritis"')
young = df.query('Age <= 20 and Medical Condition == "Arthritis"')

filtered_df = df.query('Age >= 80')
rah = filtered_df['Medical Condition'].value_counts

print(len(df))