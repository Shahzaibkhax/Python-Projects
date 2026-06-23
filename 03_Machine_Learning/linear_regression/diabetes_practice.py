import matplotlib.pyplot as plt 
import numpy as np
from sklearn .datasets import make_regression
from sklearn .linear_model import LinearRegression
from sklearn .metrics import mean_squared_error , r2_score
from sklearn.model_selection import train_test_split

X , y = make_regression(
    n_samples=100 , n_features=1 , noise=15.0 , random_state= 42 
)

X_train, X_test , y_train , y_test = train_test_split(
    X , y , test_size= 0.2 , random_state= 42 
)

model = LinearRegression()

model.fit (X_train , y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test , predictions)

r2 = r2_score( y_test , predictions)

print("---Scikit-Learn Practice Result ---")

print(f"model slope (β₁): {model.coef_[0] : 4f}")

print(f"model intercept (β₀): {model.intercept_ : .4f}")

print (f"means squared Error (mse): {mse:.2f}")

print(f"R² fit score (0 to 1): {r2 : .4f}")

print("--------------------------------------------\n")

plt.scatter (X_test , y_test , color = "blue" , label = "Actual Patients")

plt.plot( X_test, predictions , color = "red" , linewidth=2, label = "AI best fit line")

plt.title("linear regression practice ( BMI vs Disease progression )")

plt.xlabel("patient BMI feature (scaled)")

plt.ylabel ( " diseases progression score")

plt . legend()

plt.show()


