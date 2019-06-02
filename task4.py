def task5():
    for a in range(1,999):
        for b in range(1,999):
            num = str(a*b)
            if (num == num[::-1])and(int(num)>900000):
                result = num
                break
    print(result)
task5()
