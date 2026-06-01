import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

df = pd.read_csv("cleaned.csv")

features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
target = "Survived"

df["Sex"] = df["Sex"].map({"male" : 0, "female" : 1})

x = df[features]
y = df[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print(x_train.shape)
# print(y_train.shape)

model = LogisticRegression()
model.fit(x_train, y_train)


prediction = model.predict(x_test)
accurancy = accuracy_score(y_test, prediction)
print(f"Model Accurancy: {accurancy:.2%}")
print(classification_report(y_test, prediction))