import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Load data
df = pd.read_csv('archive/movies.csv', encoding='latin1')

# 2. Convert every column to object type temporarily to avoid the strict 'str' error
df = df.astype(object)

# 3. Clean specific columns
df['Year'] = df['Year'].astype(str).str.replace(r'[()]', '', regex=True)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0)

df['Votes'] = pd.to_numeric(df['Votes'].astype(str).str.replace(',', ''), errors='coerce').fillna(0)
df['Duration'] = pd.to_numeric(df['Duration'].astype(str).str.replace(' min', ''), errors='coerce').fillna(0)

# 4. Drop and Fill
df.dropna(subset=['Rating'], inplace=True)
df.fillna(0, inplace=True)

# 5. Encode labels
le = LabelEncoder()
cols_to_encode = ['Genre', 'Director', 'Actor 1']
for col in cols_to_encode:
    df[col] = le.fit_transform(df[col].astype(str))

# 6. Save
df.to_csv('cleaned_movies.csv', index=False)
print("Data cleaned successfully!")