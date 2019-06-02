import numpy as np

def task16():
    a = 2**1000
    b = str(a)
    c = list(b)
    d = [int(n) for n in b]
    print(np.sum(d))

   
task16()
