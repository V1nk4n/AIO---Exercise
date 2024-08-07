import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./AIO2024/AIO-Exercise/module02/week04/advertising.csv")
print(data.corr())


def correlation(x, y):
    N = len(x)
    numerator = 0
    denominator = 0
    numerator = N*np.sum(x*y) - np.sum(x)*np.sum(y)
    denominator = np.sqrt(N*np.sum(x**2)-np.sum(x)**2) * \
        np.sqrt(N*np.sum(y**2)-np.sum(y)**2)
    return np.round(numerator/denominator, 2)


plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidths=.5, cmap='coolwarm')
plt.show()
