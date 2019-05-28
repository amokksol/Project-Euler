import numpy as np
import pandas

def task6():
    a = 0
    b = []
    for i in range(101):
        i = i**2
        a = a+i
    for k in range(101):
        b.append(k)
        k+=1
    c = np.sum(b)**2
    print(c-a)

task6()
