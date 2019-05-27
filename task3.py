def task3(a):
    x = []
    for i in range(a, 1, -1):
        if i < 10 and i%10==5:
            continue
        for k in x:
            if k*k-1<i:
                x.append(i)
                break
            if i%k == 0:
                break
        else:
            x.append(i)
    print(x)
        
task3(100)
