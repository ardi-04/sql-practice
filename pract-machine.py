from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics  import classification_report
from sklearn.metrics  import accuracy_score
from sklearn.tree  import DecisionTreeClassifier
import pandas as pd




iris = load_iris()


X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2 ,random_state=5, stratify=y)

model = LogisticRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
print(accuracy)
print(classification_report(y_test, prediction))


tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)
prediction = tree_model.predict(X_test)
tree_accurancy = accuracy_score(y_test, prediction)
print(tree_accurancy )
print(classification_report(y_test, prediction))