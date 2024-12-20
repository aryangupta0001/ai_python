import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./exp-6_iris_dataset_visualisation/iris_data.csv")
print(df.head())

print(df.shape)
print(df.dtypes)
x_axis = 'sepal_length'
y_axis = 'sepal_width'
title = "Sepal Length v/s Width"

# plt.plot(df[x_axis], df[y_axis], marker = 'o', linestyle = '-', color = 'b')
# plt.title("Iris Data Projection")
# plt.xlabel(x_axis)
# plt.ylabel(y_axis)

plt.figure()

ax = plt.axes()
ax.scatter(df[x_axis], df[y_axis])
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title(title)

plt.show()