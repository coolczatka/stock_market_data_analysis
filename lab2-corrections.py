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
x1 = df['Date'].apply(lambda a: dt.strptime(a, '%Y-%m-%d'))


x_smaller = df['Date'].values[-700:]
y_smaller = df['Close'].values[-700:]
x1_smaller = df['Date'].apply(lambda a: dt.strptime(a, '%Y-%m-%d'))[-700:]

log_ret = []

for i in range(len(y)-1):
    lr = np.log(y[i+1]/y[i])
    log_ret.append(lr)

lr1 = (log_ret - np.mean(log_ret)) / np.std(log_ret)

log_ret_s = []
for i in range(len(y_smaller)-1):
    lr = np.log(y_smaller[i+1]/y_smaller[i])
    log_ret_s.append(lr)

plt.figure(1)
(n, bins, patches) = plt.hist(lr1)
plt.title('Histogram stóp zwrotu')
plt.show()


y2 = n / len(y)
bins2 = []
st = bins[0]
for b in bins[1:]:
    bins2.append((b+st)/2)
    st=b


plt.figure(2)
plt.bar(bins2, y2, width=4.5)
plt.title('Znormalizowany histogram stóp zwrotu')
plt.show()

whiteNoise = np.random.normal(0, np.std(lr1), len(x))

plt.figure(2)
(n, bins, patches) = plt.hist(whiteNoise)
plt.title('Histogram białego szumu')
plt.show()

yn = n / len(y)
bins3 = []
st = bins[0]
for b in bins[1:]:
    bins3.append((b+st)/2)
    st=b

plt.figure(3)
plt.bar(bins3, yn, width=0.8)
plt.title('Znormalizowany histogram białego szumu')
plt.show()

print(f"Oryginalny: Kurtoza {stats.kurtosis(lr1)} Skosnosc {stats.skew(lr1)}")
print(f"Zaszumiony: Kurtoza {stats.kurtosis(whiteNoise)} Skosnosc {stats.skew(whiteNoise)}")


y2sk = rozkl_sk(y2)
y2nsk = rozkl_sk(yn)

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
