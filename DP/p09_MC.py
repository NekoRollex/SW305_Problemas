import random

def CaminoMinimo(A, m, n):
    r = [[None for j in range(n)] for i in range(m)]

    r[0][0] = A[0][0]
    for i in range(1, m):
        r[i][0] =  A[i][0] + r[i-1][0]    
    for j in range(1, n):
        r[0][j] =  A[0][j] + r[0][j-1]

    return AuxCaminoMinimo(A, r, m-1, n-1)

def AuxCaminoMinimo(A, r, i, j):
    if r[i][j] != None:
        return r[i][j]
    
    min = None
    if i>0:
        min = AuxCaminoMinimo(A, r, i-1, j)
    if j>0:
        b = AuxCaminoMinimo(A, r, i, j-1)
        if min != None:
            if min>b:
                min = b
        else:
            min = b
    r[i][j] = min + A[i][j]

    return r[i][j]

m = random.randint(1, 10)
n = random.randint(1, 10)

A = [[random.randint(1, 10) for j in range(n)] for i in range(m)]

minpath = CaminoMinimo(A, m, n)

print(A)
print(minpath)