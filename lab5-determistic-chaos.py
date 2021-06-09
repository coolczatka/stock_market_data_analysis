import matplotlib.pyplot as plt
import numpy as np
import random


fx = lambda x: 3.7*x*(1-x)
# epsilon = .001
plotStartStep = 59
maxStep = 60
x1 = x1s = 0.34568885
x2 = x2s = x1 + 1e-8

fx1 = []
fx2 = []

step = 1

while(True):
    fx1.append(fx(x1))
    fx2.append(fx(x2))
    print(abs(fx1[-1]-fx2[-1]))

    if(step == maxStep): # or abs(fx1[-1]-fx2[-1]) > epsilon):
        break
    x1 = fx1[-1]
    x2 = fx2[-1]
    step += 1

fargx = np.linspace(0, 1, 100)
fvalues = fx(fargx)

plt.figure()
plt.title(f"x1_0 = {x1s}, x2_0 = {x2s}, krokStart = {plotStartStep}, krok = {step}")
plt.plot(fargx, fvalues, 'b-')
plt.plot(fargx, fargx, 'y-')

x1s = [x1s] + fx1
y1s = [0] + fx1
x2s = [x2s] + fx2
y2s = [0] + fx2


for i in range(plotStartStep, len(x1s)):
    plt.plot([x1s[i-1], x1s[i-1]], [y1s[i-1], y1s[i]], 'ro-')
    plt.plot([x1s[i-1], x1s[i]], [y1s[i], y1s[i]], 'ro-')
    plt.plot([x2s[i-1], x2s[i-1]], [y2s[i-1], y2s[i]], 'go-')
    plt.plot([x2s[i-1], x2s[i]], [y2s[i], y2s[i]], 'go-')
plt.show()

print(fx1)
print(fx2)

# plt.plot([fx1[i-1], fx1[i-1]], [fx1[i-1], fx1[i]], 'ro-')
#     plt.plot([fx1[i-1], fx1[i]], [fx1[i], fx1[i]], 'ro-')