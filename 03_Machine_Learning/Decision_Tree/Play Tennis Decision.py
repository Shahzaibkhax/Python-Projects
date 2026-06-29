from sklearn.tree import DecisionTreeClassifier , export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Outlook: 0=Sunny, 1=Overcast, 2=Rain
# Humidity: 0=Normal, 1=High
# Wind: 0=Weak, 1=Strong

X = [
    [0,1,0],
    [0,1,1],
    [1,1,0],
    [2,0,0],
    [2,0,0],
    [2,1,1],
    [1,0,1],
    [0,1,0],
    [0,0,0],
    [2,0,0],
    [0,0,1],
    [1,0,1],
    [1,1,0],
    [2,1,1],
]

y = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0] #Do not play , 1 = play 


X_train , X_test, y_train , y_test = train_test_split(
    X , y , test_size= 0.2 ,  random_state= 42
)

model = DecisionTreeClassifier(max_depth= 3 , criterion="gini",random_state= 42 )

model.fit(X_train, y_train)

features_names = [ "Outlook" , "Humidity " , "Wind" ]
print(export_text(model,feature_names=features_names))

preds = model.predict(X_test)
print ("Accuracy :" , accuracy_score(y_test,preds))

new_day = [[2,0,0]]
result = model.predict(new_day)
print("play tennis ?", "Yes" if result[0] == 1 else "NO")

for name , imp in zip ( features_names , model.feature_importances_):
    print(f"{name} : {imp : .2f}")

    