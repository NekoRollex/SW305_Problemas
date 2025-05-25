def Fibonacci(n):
    r = [None for i in range (n+1)]

    for j in range(n+1):
        if r[j] == None:
            if j== 0:
                r[0] = 0
            elif j == 1:
                r[1] = 1
            else:
                r[j] = Fibonacci(n-1) + Fibonacci(n-2)
    
    return r[n]

f = Fibonacci(5)
print(f)