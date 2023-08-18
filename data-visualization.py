import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creates 100 equally spaced values between 0 and 10 using the NumPy library's linspace sets. This operation is often used to specify a range for the x-axis of the chart.
x = np.linspace(0, 10, 100)

# The expression np.sin(x) calculates the sine of the given x values using the NumPy library's sin function. Here x is a NumPy array containing 100 values between 0 and 10 created in the previous code. That is, this expression calculates the sine values corresponding to x values between 0 and 10.
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Converting data to a DataFrame
data = pd.DataFrame({'x': x, 'y': y})

# Draw
plt.figure(figsize=(10, 6))  # size of drawing
plt.scatter(data['x'], data['y'], label='Veri Noktaları')  # dot of drawing
plt.plot(data['x'], np.sin(data['x']), color='red', label='Sinüs Fonksiyonu')  # drawing of sin func.
plt.title('Örnek Veri Görselleştirmesi')
plt.xlabel('x Değeri')
plt.ylabel('y Değeri')
plt.legend()
plt.grid(True)
plt.show()
