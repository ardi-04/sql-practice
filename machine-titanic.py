import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("cleaned.csv")

features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
target = "Survived"

df["Sex"] = df["Sex"].map({"male" : 0, "female" : 1})

x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print(x_train.shape)
# print(y_train.shape)

#Logistic Regression
# model = LogisticRegression()
# model.fit(x_train, y_train)


# prediction = model.predict(x_test)
# accurancy = accuracy_score(y_test, prediction)
# print(f"Model Accurancy: {accurancy:.2%}")
# print(classification_report(y_test, prediction))

# probabilities = model.predict_proba(x_test)
# print(probabilities[:5])

#Decision Tree
# tree_model = DecisionTreeClassifier(random_state=42)
# tree_model.fit(x_train, y_train)
# tree_predictions = tree_model.predict(x_test)
# tree_accuracy = accuracy_score(y_test, tree_predictions)
# print(f"Decision Tree Accuracy: {tree_accuracy:.2%}")

#Random Forest
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_model.fit(x_train, y_train)
# rf_predictions = rf_model.predict(x_test)
# rf_accuracy = accuracy_score(y_test, rf_predictions)
# print(f"Random Forest Accuracy: {rf_accuracy:.2%}")

# rf_train_predictions = rf_model.predict(x_train)
# rf_train_accuracy = accuracy_score(y_train, rf_train_predictions)
# print(f"RF Training accuracy: {rf_train_accuracy:.2%}")
# print(f"RF Test accuracy: {rf_accuracy:.2%}")


#K-nearest neigbour
# from sklearn.neighbors import KNeighborsClassifier

# knn_model = KNeighborsClassifier(n_neighbors=53)
# knn_model.fit(x_train, y_train)
# knn_predictions = knn_model.predict(x_test)
# knn_accuracy = accuracy_score(y_test, knn_predictions)
# print(f"KNN Accuracy: {knn_accuracy:.2%}")

#Cross Splitting

from sklearn.model_selection import cross_val_score

scores = cross_val_score(LogisticRegression(), x, y, cv=5)
print(f"Individual scores: {scores}")
print(f"Mean accuracy: {scores.mean():.2%}")
print(f"Standard deviation: {scores.std():.2%}")