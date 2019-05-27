def task2(num):
    a = 0
    b = 1
    x = []
    for i in range(num):
        a,b = b, a + b
        print(a)
    if a%2==0:
        x.append(a)
    print(x)
task2(10)
