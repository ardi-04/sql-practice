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
    

df = clean_data("train.csv")
print(df.isnull().sum())
print(df.columns.tolist())

