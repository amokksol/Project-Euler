import numpy as np
def task1(a):
    b = []
    for i in range(a):
        if i%3==0:
            b.append(i)
        elif i%5==0:
            b.append(i)
    c = np.sum(b)
    print(c)
task1(1000)
