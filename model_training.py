import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv('cleaned_movies.csv')

# Select Features and Target
X = df[['Year', 'Duration', 'Genre', 'Votes', 'Director', 'Actor 1']]
y = df['Rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, 'movie_model.pkl')
print("Model trained and saved as movie_model.pkl")