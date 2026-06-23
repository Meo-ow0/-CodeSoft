import pandas as pd

# 1. Load the dataset
df = pd.read_csv('creditcard.csv')

# 2. See the first few rows of data
print("Here is the first look at your data:")
print(df.head())

# 3. Check for class imbalance (The most important step for fraud detection)
print("\nClass distribution (0=Normal, 1=Fraud):")
print(df['Class'].value_counts())