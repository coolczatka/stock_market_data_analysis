import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import random
from datetime import datetime as dt
from matplotlib.ticker import FormatStrFormatter

def rozkl_sk(y):
    sum_sk = []
    suma = 0
    for i in y:
        suma += i
        sum_sk.append(1-suma)
    return sum_sk

df = pd.read_csv('PG.csv', sep=',')
# Date,Open,High,Low,Close,Adj Close,Volume

x = df['Date'].values
y = df['Close'].values

whiteNoice = np.random.normal(np.mean(y), np.std(y), len(x))
noisedY = y+whiteNoice

plt.figure(1)
tup = plt.hist(y)
plt.title('Histogram danych oryginalnych')
plt.show()
y2 = tup[0]
y2 = y2 / len(y)

plt.figure(2)
plt.bar(range(len(y2)),y2)
plt.title('Znormalizowany histogram danych oryginalnych')
plt.show()
#
plt.figure(3)
tup2 = plt.hist(noisedY)
plt.title('Histogram danych wygenerowanych')
plt.show()
ynoised2 = tup2[0]
ynoised2 = ynoised2 / len(y)

plt.figure(4)
plt.bar(range(len(ynoised2)),ynoised2)
plt.title('Znormalizowany histogram danych wygenerowanych')
plt.show()

print(f"Oryginalny: Kurtoza {stats.kurtosis(y)} Skosnosc {stats.skew(y)}")
print(f"Zaszumiony: Kurtoza {stats.kurtosis(noisedY)} Skosnosc {stats.skew(noisedY)}")

y2sk = rozkl_sk(y2)
y2nsk = rozkl_sk(ynoised2)

plt.figure(5)
plt.plot(y2sk)
plt.title('Rozklad skumulowany danych oryginalnych')
plt.show()

plt.figure(6)
plt.plot(y2nsk)
plt.title('Rozklad skumulowany danych wygenerowanych')
plt.show()

plt.plot(y2sk, 'r')
plt.plot(y2nsk, 'b')

plt.title('Rozkłady skumulowane')
plt.yscale('log')
plt.xscale('log')
plt.show()
