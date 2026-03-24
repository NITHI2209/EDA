import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:/customers-100.csv")
print(df)
print(df.describe())
print(df.head())
print(df.tail(10))
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.nunique())
print(df.duplicated())
