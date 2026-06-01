print()
print("MISSING")
print() 
#handling missing values
print(df.isnull().sum())
df["grade"] = df["grade"].fillna(df["grade"].mean())
print(df.isnull().sum())