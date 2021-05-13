from statsmodels.graphics import tsaplots
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as dt
from scipy import stats

df = pd.read_csv('PG.csv', sep=',')
# Date,Open,High,Low,Close,Adj Close,Volume
x = df['Date'].values
y = df['Close'].values
x1 = df['Date'].apply(lambda a: dt.strptime(a, '%Y-%m-%d'))

log_ret = []
for i in range(len(y)-1):
    lr = np.log(y[i+1]/y[i])
    log_ret.append(lr)

lr1 = (log_ret - np.mean(log_ret)) / np.std(log_ret)


#plot autocorrelation function
fig = tsaplots.plot_acf(lr1, zero=False, lags=100, title="Autokorelacja danych giełdowych (P&G)")
plt.show()

whiteNoise = np.random.normal(0, np.std(lr1), len(x))

fig = tsaplots.plot_acf(whiteNoise, zero=False, lags=100, title="Autokorelacja białego szumu")
plt.show()

lr1_abs = np.abs(lr1)
wn_abs = np.absolute(whiteNoise)

fig = tsaplots.plot_acf(lr1_abs, zero=False, lags=100, title="Autokorelacja modułu danych giełdowych (P&G)")
plt.show()

fig = tsaplots.plot_acf(wn_abs, zero=False, lags=100, title="Autokorelacja modułu białego szumu")
plt.show()

plt.psd(lr1)
plt.title("Widmo mocy dla danych giełdowych (P&G)")
plt.show()

plt.psd(whiteNoise)
plt.title("Widmo mocy dla białego szumu")
plt.show()

plt.psd(lr1_abs)
plt.title("Widmo mocy dla modułu danych giełdowych (P&G)")
plt.show()

plt.psd(wn_abs)
plt.title("Widmo mocy dla modułu białego szumu")
plt.show()
