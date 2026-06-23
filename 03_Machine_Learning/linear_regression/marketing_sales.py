import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.model_selection import train_test_split

X = np.array ([[1.0], [2.0], [3.0], [4.0], [5.0],[6.0],[7.0],[8.0],[9.5], [10.0]])
y = np.array([12, 19, 26, 33, 38, 49, 53, 62, 71, 78])

X_train, X_test , y_train , y_test = train_test_split (
    X , y , test_size= 0.2 , random_state= 42 
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions= model.predict(X_test)

mse = mean_squared_error(y_test,predictions)

r2= r2_score(y_test,predictions)


print("--- Marketing ROI Model Results ---")
print(f"Model Slope (β₁): {model.coef_[0]:.4f}")

print(f"Model Intercept (β₀): {model.intercept_:.4f}")

print(f"Means squared Error (mse) : {mse : .2f}")
print (f"r2 fit score ( 0 to 1 ): {r2 : .4f}\n")

custom_spend = [[5.5]]

predicted_sale = model.predict(custom_spend)

print (f"predicted sales for a $5,500 ad spend : ${predicted_sale[0]:.2f}k (${predicted_sale[0]*1000:,.0f})")


plt.scatter(X, y, color="purple" , label="historical data ")

plt.plot(X_test , predictions, color = "orange",linewidth=2,label="AI prediction trend ")

plt.title (" Ad spend vs total sales revenue")
plt.xlabel ("ad budget (in thousands of $ )")
plt.ylabel("Sales revenue (in thousands of $)")

plt.legend()

plt.show()