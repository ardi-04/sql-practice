import pandas  as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


df = pd.read_csv("games.csv")

df["Number of Reviews"] = (df["Number of Reviews"].astype(str)
.str.replace(",", "", regex=False)
.str.replace("K","e3", regex=False)
.str.replace("M", "e6", regex=False)
.astype(float)
)

feature = df[["Number of Reviews"]]
target = df["Rating"]


X = feature
y = target >= 4

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=10, stratify=y)

model = LogisticRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
accurancy = accuracy_score(y_test, prediction)
print(f"The accurancy is: {accurancy:.2%}")
print(classification_report(y_test, prediction))


tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)
tree_prediction = tree_model.predict(X_test)
tree_accurancy = accuracy_score(y_test, tree_prediction)

print(f"The accurancy is: {tree_accurancy:.2%}")
print(classification_report(y_test, tree_prediction))