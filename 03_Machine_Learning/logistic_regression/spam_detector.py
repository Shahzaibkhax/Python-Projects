import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# 1. Fixed the missing commas at the end of rows here!
X = np.array([
    [1, 200, 0],
    [8, 50, 1],
    [2, 300, 0],
    [12, 30, 1],
    [0, 400, 0],
    [10, 45, 1]
])

y = np.array([0, 1, 0, 1, 0, 1])

# Using test_size=0.33 to make sure there are enough samples to run
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

print("--- Model Predictions & Probabilities ---")
print(f"Test Set Predictions (0 or 1): {predictions}")
print(f"Raw Probabilities:\n{probabilities}\n")

print("--- Evaluation Matrix Report ---")
# Fixed the accuracy print call parameters and colon symbol!
print(f"Accuracy Score: {accuracy_score(y_test, predictions):.2%}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

new_email = np.array([[7, 40, 1]])
predicted_class = model.predict(new_email)
spam_prob = model.predict_proba(new_email)[0][1]

print("\n--- Incoming New Email Analysis ---")
print(f"AI Classification: {'Spam' if predicted_class[0] == 1 else 'Not Spam'}")
print(f"Calculated Spam Probability: {spam_prob:.2%}")

