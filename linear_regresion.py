import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("homeprices.csv")
print(df)

reg = linear_model.LinearRegression()
reg.fit(df[["area"]],df.price)

plt.xlabel("area(sq ft)")
plt.ylabel("price(US$)")
plt.scatter(df.area,df.price,color="red",marker="+")
plt.plot(df.area,reg.predict(df[["area"]]),color="blue")
plt.show()

def prediction(x):
    return reg.predict([[x]]) 

print(prediction(3300))#x

print(reg.coef_)#m
print(reg.intercept_)#b

#proof---------------------------------------
#y = m*x + b
print(135.78767123*3300+180616.43835616432)