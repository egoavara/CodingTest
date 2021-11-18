# %%
import matplotlib.pyplot as plt
import numpy as np
from math import *

def fny(x):
    return 12 + 6*cos(2*pi*x/20)
def fny2(x):
    return 10 + 5*cos(2*pi*x/20)

t = [i * 2.5 for i in range(9)]
y = np.vectorize(fny2)(t)
y[0] = fny(t[0])

print(t)
print(y)


plt.plot(t, y)