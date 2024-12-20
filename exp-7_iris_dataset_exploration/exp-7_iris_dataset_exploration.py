import pandas as pd

df = pd.read_csv("./exp-7_iris_dataset_exploration/iris_data.csv")
print(df.head())

print(df.shape[0])
print(df.columns.tolist())
print(df.dtypes)