import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Get the directory where this script (main.py) is located
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'IRIS.csv')

# Step 1: Read the data using the absolute path
df = pd.read_csv(file_path)

# ... (rest of your code stays exactly the same)
"""
Project: Iris Flower Classification
Goal: Build a machine learning model to categorize iris species.
Author: [Your Name]
Method: Decision Tree Classifier
"""
import matplotlib.pyplot as plt

# Simple check of data distribution
df['species'].value_counts().plot(kind='bar')
plt.title('Distribution of Iris Species')
plt.show()