import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("jordon_quinn_110H.csv")


df["race_index"] = range(1, len(df) + 1)

reg = linear_model.LinearRegression()
reg.fit(df[["hurdle_height", "race_index"]], df["time"])

print(reg.coef_)
print(reg.intercept_)


prediction = reg.predict([[42, 28]])
print(prediction)