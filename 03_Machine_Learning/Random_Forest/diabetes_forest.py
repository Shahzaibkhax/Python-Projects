from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , classification_report 
import numpy as np

from sklearn.datasets import load_diabetes
data = load_diabetes()

X , y = data.data , (data.target > 140).astype (int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(
    n_estimators=100, 
    max_depth=None,   
    max_features='sqrt', 
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

probs = model.predict_proba(X_test)

print ("Accuracy:" , accuracy_score(y_test,predictions))
print(classification_report(y_test,predictions))

features_names = data.feature_names
importances = model.feature_importances_

sorted_idx = np.argsort(importances)[::-1]

print("\nFeature importance:")
for i in sorted_idx:
    print(f"{features_names[i]}: {importances[i]:.3f}")

new_patient = [X_test[0]]
result = model.predict(new_patient)
prob = model.predict_proba(new_patient)[0][1]

print(f"\nDiabetes risk : {'YES' if result[0]==1 else 'No'}({prob:.0%} confidence)")
