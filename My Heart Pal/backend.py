import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load the dataset
heart_data = pd.read_csv('D:/Project/Python AI Projects/My Heart Pal/heart.csv')

# Checking for missing values
heart_data.isnull().sum()

# Statistical measures about the data
heart_data.describe()

# Checking the distribution of Target Variable
heart_data['target'].value_counts()

# Splitting the data into features (X) and target variable (Y)
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training the Logistic Regression model
model = LogisticRegression(max_iter=10)  # Increase max_iter to allow more iterations
model.fit(X_train_scaled, Y_train)

# Making predictions on training data
X_train_prediction = model.predict(X_train_scaled)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data:', training_data_accuracy)

# Making predictions on test data
X_test_prediction = model.predict(X_test_scaled)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data:', test_data_accuracy)
