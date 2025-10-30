import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import joblib

# Load the dataset
data = pd.read_csv("data/resumes/career_dataset.csv")
data = data.dropna()


# Combine skills into one text string
X = data["skills"]
y = data["career"]

# Convert text into numerical features
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train a simple model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save model and vectorizer
with open("models/career_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model trained and saved successfully!")
