import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime as dt
from matplotlib.ticker import FormatStrFormatter

df = pd.read_csv('PG.csv', sep=',')
# Date,Open,High,Low,Close,Adj Close,Volume

x = df['Date'].values
y = df['Close'].values

x1 = df['Date'].apply(lambda a: dt.strptime(a, '%Y-%m-%d'))

plt.figure()
plt.plot(x1, y)
plt.title("Cena akcji P&G (skala liniowa)")
plt.xlabel('Czas')
plt.ylabel('Cena akcji')
plt.show()

plt.figure()
plt.plot(x1, y)
plt.title("Cena akcji P&G (skala półlogarytmiczna)")
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.d'))
plt.xlabel('Czas')
plt.ylabel('Cena akcji')
plt.show()

# ---------------------------------------------------------
log_ret = []
for i in range(len(y)-1):
    lr = np.log(y[i+1]/y[i])
    log_ret.append(lr)

print (len(x), len(log_ret))

plt.figure()
plt.plot(x1[:-1], log_ret, linewidth=0.5)
plt.title("Logarytmiczna stopa zwrotu akcji P&G")
# plt.yscale('log')
# plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.d'))
plt.xlabel('Czas')
plt.ylabel('Wartość stopy zwrotu')
plt.show()

# ---------------------------------------------------------

# scaler = StandardScaler()
# scaler.fit(log_ret)
# lr1 = scaler.transform(log_ret)

lr1 = (log_ret - np.mean(log_ret)) / np.std(log_ret)
print(np.std(lr1))
print(np.mean(lr1))

plt.figure(5)
plt.plot(x1[:-1], lr1, linewidth=0.5)
plt.xlabel('Czas')
plt.ylabel('Wartość stopy zwrotu')
plt.title("Znormalizowana logarytmiczna stopa zwrotu")

plt.show()

whiteNoice = np.random.normal(0, np.std(y), len(x))

plt.figure(6)
plt.plot(range(len(whiteNoice)), whiteNoice, linewidth=0.5)
plt.title("Biały szum")
plt.show()

suma_sk = []
suma_sk_n = []
suma = 0
suma_n = 0

for w in whiteNoice:
    suma_n += w
    suma_sk_n.append(suma_n)

for l in log_ret:
    suma += l
    suma_sk.append(suma)

plt.figure(7)
plt.plot(x1[:-1], suma_sk, linewidth=0.8)
plt.title("Suma skumulowana stóp zwrotu danych giełdowych")
plt.xlabel('Czas')
plt.ylabel('Wartość sumy skumulowanej')

plt.show()

plt.figure(8)
plt.plot(x1, suma_sk_n, linewidth=0.8)
plt.title("Suma skumulowana białego szumu")
plt.ylabel('Wartość sumy skumulowanej')
plt.show()