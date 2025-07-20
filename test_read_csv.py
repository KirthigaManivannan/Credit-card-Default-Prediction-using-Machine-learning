import os
import pandas as pd

# Print current working directory
print("Current working directory:", os.getcwd())

# List files in the current directory
print("Files in the directory:", os.listdir())

# Attempt to read the CSV file
try:
    df = pd.read_csv('client.csv')
    print("CSV File Loaded Successfully!")
    print(df.head())
except Exception as e:
    print(f"Error reading CSV file: {e}")
