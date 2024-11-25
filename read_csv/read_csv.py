import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("iris_data.csv").head(10)
print(df)
x_axis = 'sepal_length'
y_axis = 'sepal_width'

plt.plot(df[x_axis], df[y_axis], marker = 'o', linestyle = '-', color = 'b')
plt.title("Iris Data Projection")
plt.xlabel(x_axis)
plt.ylabel(y_axis)

pie_data = np.array([10, 20, 30, 40])
pie_labels = ['a', 'b', 'c', 'd']

plt.figure()
plt.title("Pie Chart Example")
plt.pie(pie_data, labels=pie_labels)
plt.grid(True)

plt.show()