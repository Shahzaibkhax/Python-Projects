import numpy as np 
from sklearn.tree import DecisionTreeClassifier , export_text
from sklearn .metrics import accuracy_score
from sklearn.model_selection import train_test_split


# 1. prepare historical project data 
# Features : [ Tech_Stack_Match (0/1) , Good_Budget (0/1), TimeLine_Days]

X=[
    [1,1,30],  # Wordpress site , greate budget , 30 days -> Accept
    [0,0,5],
    [1,0,45],  # python script , low budget , only 45 days -> Accept    
    [0,1,3],
    [1,1,14],
    [1,0,7],   # Wordpress site , terrible bufget, 7 days -> Decline

]

y = [ 1, 0, 1, 0, 1, 0]

# 0 = Decline project , 1 = Accept project 

X_train ,  X_test , y_train , y_test = train_test_split(

    X , y , test_size = 0.2 ,random_state= 42 
)

model= DecisionTreeClassifier( max_depth = 2 , criterion='gini',random_state = 42)
model.fit(X_train , y_train)

feature_names = [ 'TechMatch' , 'GoodBuget' , 'TimeLineDays']
print('---AI project Selection Logic Tree ---')
print(export_text(model, feature_names=feature_names))

preds = model.predict(X_test)
print(f"Model Evaluation Accurancy : {accuracy_score(y_test,preds):.2%}\n")

new_inquiry = [[1,0,7]]
decision = model.predict(new_inquiry)

print("--- Live Inquiry Analysis ---")
print(f"AI Business Recommendation: {' ACCEPT AND SIGN CONTRACT' if decision[0] == 1 else ' DECLINE PROJECT'}")

print("\n--- Feature Importance Breakdown ---")
for name, imp in zip(feature_names, model.feature_importances_):
    print(f"{name}: {imp:.2%}")

