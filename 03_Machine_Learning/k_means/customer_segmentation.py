import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Features: [Total_Spend_$, Number_of_Orders]
X = [
    [15.0, 1],   # Small spender, single purchase
    [1200.0, 25],# High spender, power shopper
    [22.0, 2],   # Small spender, low activity
    [950.0, 18], # High spender, frequent buyer
    [40.0, 1],   # Small spender, cautious buyer
    [1500.0, 30] # VIP client, massive activity
]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=2 , random_state= 42, n_init= 10)
model.fit(X_scaled)

label = model.labels_

print("--- E-Commerce K-Means Segmentation Engine ---")
for i, customer in enumerate(X):
    print(f"Customer Profile {customer} -> Assigned to Group Layer: {label[i]}") 


new_shopper = scaler.transform([[500.0, 1]])
assigned_cluster = model.predict(new_shopper)

print("\n--- Live Traffic Categorization ---")
print(f"New Customer Target Group -> Layer {assigned_cluster[0]}")