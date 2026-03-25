import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:/customers-100.csv")
print(df.fillna(0))
print(df.drop_duplicates())
print(df.isnull().sum())
#df.drop(["columun_name"])