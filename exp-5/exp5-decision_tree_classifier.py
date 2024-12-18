import pandas as pd
import matplotlib.pyplot as ptt
from sklearn.model_selection import train_test_split
import category_encoders as ce
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

data = "./exp-5/car_evaluation.csv"
df = pd.read_csv(data, header = None)

col_names= ['buying', 'maint', 'doors', 'person', 'lug_boot', 'safety', 'class']
df.columns = col_names

print(col_names)
print(df.head())
x = df.drop(['class'], axis = 1)
y = df['class']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

print(x_train.shape, x_test.shape)


encoder = ce.OrdinalEncoder(cols=['buying', 'maint', 'doors', 'person', 'lug_boot', 'safety'])

x_train = encoder.fit_transform(x_train)
x_test = encoder.transform(x_test)


clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)

clf_gini.fit(x_train, y_train)

y_pred_gini = clf_gini.predict(x_test)


print("Model accuracy score with criterion gini index {0:0.4f}".format(accuracy_score(y_test, y_pred_gini)))


y_pred_train_gini = clf_gini.predict(x_train)
print(y_pred_train_gini)

print("Training set accuracy score : {0:0.4f}".format(accuracy_score(y_train, y_pred_train_gini)))

print("Training set score : {0:0.4f}".format(clf_gini.score(x_train, y_train)))


print("Test set score : {0:0.4f}".format(clf_gini.score(x_test, y_test)))

ptt.figure(figsize=(12, 8))
tree.plot_tree(clf_gini.fit(x_train, y_train))
ptt.show()