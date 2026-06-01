import pandas as pd

df = pd.read_csv("student.csv")
# print()
# print("SELECTING")
# print()
# #Selecting columns
# print(df["grade"])
# print(df[["name" , "grade"]])

# print("FILTERING")
# print()
# #filtering rows
# print(df[df["grade"] > 85])
# print(df[df["department"] == "Engineering"])

print()
print("MISSING")
print() 
#handling missing values
print(df.isnull().sum())
df["grade"] = df["grade"].fillna(df["grade"].mean())
print(df.isnull().sum())

# print()
# print("GROUPING")
# print()
# #Geoup By
# print(df.groupby("department")["grade"].mean())



df["passed"] = df["grade"] >= 75
df_sorted = df.sort_values("grade" , ascending=False)
print(df_sorted)


# print("HEAD")
# print(df.head())
# print()
# print("shape")
# print(df.shape)
# print()
# print("INFOS")
# print(df.info())
# print()
# print("DESCRIBE")
# print(df.describe())
# print()
# print("ISNULL")
# print(df.isnull().sum())