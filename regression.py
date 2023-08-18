import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


np.random.seed(0)
x = np.random.rand(50, 1) * 10  # 0 and 10
y = 2 * x + 1 + np.random.randn(50, 1)  # y values added to  real regression line

# x and y are prebuilt NumPy arrays and represent the x and y values of the dataset.
# The .flatten() method makes a multidimensional NumPy array one-dimensional. This makes it have a neater structure when creating Pandas DataFrame.
# The expression pd.DataFrame({'x': x.flatten(), 'y': y.flatten()}) creates a Pandas DataFrame containing the x and y values. This DataFrame consists of two columns, x column and y column. Each row has its corresponding row of x and y values.
data = pd.DataFrame({'x': x.flatten(), 'y': y.flatten()})

# Creating Regression
regression_model = LinearRegression()
regression_model.fit(x, y)

# Drawring regression lineat
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], label='Veri Noktaları')
plt.plot(x, regression_model.predict(x), color='red', label='Regresyon Doğrusu')
plt.title('Veri Regresyonu Örneği')
plt.xlabel('x Değeri')
plt.ylabel('y Değeri')
plt.legend()
plt.grid(True)
plt.show()
