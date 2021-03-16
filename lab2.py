import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import random
from datetime import datetime as dt
from matplotlib.ticker import FormatStrFormatter

df = pd.read_csv('PG.csv', sep=',')
# Date,Open,High,Low,Close,Adj Close,Volume

x = df['Date'].values
y = df['Close'].values

whiteNoice = np.random.normal(0, 1, len(x))
noisedY = y+whiteNoice

plt.figure(1)
plt.hist(y)
plt.title('Histogram danych oryginalnych')
plt.show()

plt.figure(2)
plt.hist(y, density=True)
plt.title('Znormalizowany histogram danych oryginalnych')
plt.show()

plt.figure(3)
plt.hist(noisedY)
plt.title('Histogram danych zaszumionych')
plt.show()

plt.figure(4)
plt.hist(noisedY, density=True)
plt.title('Znormalizowany histogram danych zaszumionych')
plt.show()

print(f"Oryginalny: Kurtoza {stats.kurtosis(y)} Skosnosc {stats.skew(y)}")
print(f"Zaszumiony: Kurtoza {stats.kurtosis(noisedY)} Skosnosc {stats.skew(noisedY)}")
