import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 101)
l =[]
for i in x:
    if i < 0:
        l.append([i, -1])
    else:
        l.append([i, 1])


        
print(np.fft.fft(l))