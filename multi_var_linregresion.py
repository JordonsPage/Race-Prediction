import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import linear_model

df = pd.read_csv("homeprices_wit_more_vars.csv")
print(df)

median_bedrooms = math.floor(df.bedrooms.median())


df.bedrooms = df.bedrooms.fillna(median_bedrooms)
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[["area","bedrooms","age"]],df.price)

print(reg.coef_)
print(reg.intercept_)

prediction=reg.predict([[3000,3,40]])

print(prediction)