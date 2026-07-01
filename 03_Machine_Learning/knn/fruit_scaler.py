from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

# Features: [Fruit_Weight_Grams, Sweetness_Scale_1_10]
X = [
    [150, 6], [160, 6], [145, 7], [155, 5],  # apples
    [290, 9], [310, 8], [300, 9], [280, 8],  # mangoes
    [180, 7], [170, 7], [190, 6], [175, 8],  # oranges
]
y = [
    "apple", "apple", "apple", "apple",
    "mango", "mango", "mango", "mango",
    "orange", "orange", "orange", "orange",
]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3,metric="euclidean" )
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Accuracy:" , accuracy_score(y_test, predictions))

for k in [ 1, 3] :
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=2)
    print(f"K={k}: accuracy={scores.mean():.3f}")

new_fruit = scaler.transform([[220, 8]])
result = model.predict(new_fruit)
print("Unknown fruit is:", result[0]) 

distances, indices = model.kneighbors(new_fruit)
print("Neighbours at distances:", distances[0].round(2))

