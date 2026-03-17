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
# scatter of actual times
plt.figure(figsize=(10, 5))
plt.scatter(df["race_index"], df["time"], c=df["hurdle_height"].map({39: "steelblue", 42: "tomato"}), 
            s=80, zorder=5)

# regression line using predicted values across all races
predicted_times = reg.predict(df[["hurdle_height", "race_index"]])
plt.plot(df["race_index"], predicted_times, color="gray", linestyle="--", label="Trend line")

# plot scatter
plt.scatter(28, prediction[0], color="gold", s=120, zorder=6, label=f"Predicted: {prediction[0]:.2f}s")

# labels
plt.xlabel("Race #")
plt.ylabel("Time (seconds)")
plt.title("110m Hurdle Race Times + Prediction")


from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='steelblue', markersize=8, label='39" (HS)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='tomato', markersize=8, label='42" (College)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='gold', markersize=8, label=f'Predicted: {prediction[0]:.2f}s'),
    Line2D([0], [0], linestyle='--', color='gray', label='Trend line'),
]
plt.legend(handles=legend_elements)
plt.tight_layout()
plt.show()