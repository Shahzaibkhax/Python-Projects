import numpy as np 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features: [Order_Amount_$, Failed_Password_Attempts, IP_Country_Matches_Shipping (0=No, 1=Yes)]

X = [
    [25.0 , 0 ,1],
    [1500.0 , 4 ,0],
    [85.0 , 0 ,1],
    [950.0 , 2 ,1],
    [40.0 , 1 ,1],
    [2000.0 , 5 ,0],
]

y = [0,1,0,1,0,1]

X_trian , X_test , y_train , y_test = train_test_split (
    X, y, test_size = 0.33, random_state= 42 , stratify=y
)

model = RandomForestClassifier(
    n_estimators = 100,
    random_state= 42
)
model.fit(X_trian,y_train)

prreds = model.predict(X_test)
print("---E-commerce Guard System Active---")
print(f"Model Detection Accuracy: {accuracy_score(y_test,prreds):.2%}\n")

new_checkout = [[50.0, 1, 0]]
verdict = model.predict(new_checkout)
risk_percentage = model.predict_proba(new_checkout)[0][1]

print("--- Live Checkout Analysis ---")
print(f"Gateway Action: {'HOLD: Flagged for Fraud Review' if verdict[0] == 1 else '✅ CAPTURE: Payment Approved'}")
print(f"Forest Risk Consensus: {risk_percentage:.2%} of internal trees voted Fraud.")

# 6. Check Feature Importances
feature_names = ['OrderAmount', 'FailedLogins', 'LocationMatch']
print("\n--- Security Vector Importances ---")
for name, imp in zip(feature_names, model.feature_importances_):
    print(f"{name}: {imp:.2%}")

