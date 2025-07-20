import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Print current working directory to verify the script location
print("Current working directory:", os.getcwd())
print("Files in the directory:", os.listdir())

# Load Data
df = pd.read_csv('client.csv')
print(df.head())  # Check if data is loaded correctly

# Data Preprocessing
X = df.drop(columns=['default_payment_next_month'])
y = df['default_payment_next_month']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')

# Save the Model
joblib.dump(model, 'credit_default_model.pkl')

