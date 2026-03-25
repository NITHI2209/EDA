import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:/customers-100.csv")
print(df)
print(df.columns)
#df["column name"] = df["column name"].astype("int")
grouped_by = df.groupby("Country")
grouped_count = grouped_by["Country"].count()
print(grouped_count)
