import pandas as pd
import numpy as np

df = pd.read_csv("data_full.csv")
#3
print("Avg rain in 2000: ")
print(df.loc[df["Year"] == 2000, "Measurement"].sum() / 365)

#4
print("Rain amount on the median day in 2000: ")
print(df.loc[df["DoY"] == df.loc[df["Year"] == 2000, "DoY"].median()])

#5
print("Rainiest month by avg: ")
print(df.groupby("Month")["Measurement"].mean().idxmax())

#6
print("Month with most rainy days: ")
print(df[df["Measurement"] > 0].groupby("Month"))