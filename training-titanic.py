import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def clean_data(filepath):
    fpath = pd.read_csv(filepath)

    fpath["Age"] = fpath["Age"].fillna(fpath["Age"].mean())
    threshold = len(fpath) * 0.5
    fpath = fpath.dropna(thresh=threshold, axis=1)
    most_frequent = fpath["Embarked"].mode()[0]
    fpath["Embarked"] = fpath["Embarked"].fillna(most_frequent)

    print(fpath.shape)
    print(fpath.info())
    fpath["high_fare"] =  fpath["Fare"] >= fpath["Fare"].mean()

    print(fpath.describe())
    print(fpath.groupby("Pclass")["Fare"].mean())
    fpath.to_csv("cleaned.csv", index=False)




    return fpath
    
df = pd.read_csv("cleaned.csv")
numeric_df = df.select_dtypes(include=['number'])
correlation = numeric_df.corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()




# survival_rate = df.groupby("Pclass")["Survived"].mean()
# print(survival_rate)

# survival_rate.plot(kind="bar")
# plt.title("Survival Rate of passenger class")
# plt.xlabel("Passenger class") 
# plt.ylabel("Survival Rate")
# plt.show()


# df["Age"].plot(kind="hist", bins=20)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.show()

# df.groupby("Sex")["Survived"].mean().plot(kind="bar")
# plt.title("Survival Rate by Sex")
# plt.show()


plt.scatter(df["Age"], df["Fare"], alpha=0.5)
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()