import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats
from scipy.signal import savgol_filter

df = pd.read_csv("data2.csv")
print(df.head())
z_scores = stats.zscore(df)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores<3).all(axis = 1)
new_df = df[filtered_entries]
print(new_df.head())

figure, axis = plt.subplots(nrows = 1,ncols = 2)

x_acc = df['accel x']
y = np.sin(x_acc) + np.random.random(x_acc.shape[0])
y_hat = savgol_filter(y, 51, 3)

readings = np.arange(start = 0, stop = x_acc.shape[0], step = 1)
axis[0].plot(readings, x_acc)
axis[1].plot(readings, y_hat)
plt.show()