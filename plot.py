import time
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x


n_values = list(range(1, 500))  
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)


plt.plot(n_values, times, label='Measured Time')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime of Function f(n)')
plt.grid(True)


coeffs = np.polyfit(n_values, times, 2)  
poly = np.poly1d(coeffs)
plt.plot(n_values, poly(n_values), label='Fitted Curve (n^2)', linestyle='--')

plt.legend()
plt.show() # the output graph of this program is saved in plot.png
