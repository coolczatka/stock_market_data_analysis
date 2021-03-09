import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
plt.show()

plt.figure()
plt.plot(x1, y)
plt.title("Cena akcji P&G (skala półlogarytmiczna)")
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.d'))
plt.show()

# ---------------------------------------------------------
log_ret = []
for i in range(len(y)-1):
    lr = np.log(y[i+1]/y[i])
    log_ret.append(lr)

#print (len(x), len(log_ret))

plt.figure()
plt.plot(x1[:-1], log_ret, linewidth=0.5)
plt.title("Logarytmiczna stopa zwrotu akcji P&G")
# plt.yscale('log')
# plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.d'))
plt.show()

# ---------------------------------------------------------

# scaler = StandardScaler()
# scaler.fit(log_ret)
# lr1 = scaler.transform(log_ret)

print(np.std(log_ret))
print(np.mean(log_ret))

lr1 = (log_ret - np.mean(log_ret)) / np.std(log_ret)
print(np.std(lr1))
print(np.mean(lr1))

plt.figure()
plt.plot(x1[:-1], lr1, linewidth=0.5)
plt.title("Znormalizowana logarytmiczna stopa zwrotu")

plt.show()