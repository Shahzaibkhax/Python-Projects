import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.model_selection import train_test_split

X = np.array([
    [15.0, 2.0, 0],
    [1200.0, 850.0, 1],
    [45.0, 5.0, 0],
    [850.0, 400.0, 1],
    [8.0, 1.5, 0],
    [2500.0, 1200.0, 1]
])

y = np.array([0, 1, 0, 1, 0, 1 ])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= 0.2 , random_state=  42
)

model = LogisticRegression()
model.fit(X_train,y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

print("--- Fraud Model Performance ---")
print(f"Test True Labels :{y_test}")
print (f"AI hard gusses: {predictions}")
print(f"Accuracy rating : { accuracy_score(y_test, predictions):.2%} \n")

print("--- Confusion Matrix ---")
print(confusion_matrix(y_test, predictions))
print("-------------------------------\n")

new_swipe = np.array([[450.0, 300.0, 0]])
predicted_status = model.predict(new_swipe)
fraud_probability = model.predict_proba(new_swipe)[0][1]

print("---- Live Transaction Alert Summary ----")
print(f"AI Decision Flags : {'fraud Block ' if predicted_status[0] == 1 else'approved'}")
print(f"calulated risk level : {fraud_probability :}.2%")

