def LCS(Lista1, Lista2, m, n):
    r = [[None for j in range(n)] for i in range(m)]
    
    return AuxLCS(Lista1, Lista2, m-1, n-1, r)

def AuxLCS(Lista1, Lista2, i, j, r):
    if i < 0 or j < 0:
        return []

    if r[i][j] != None:
        return r[i][j]
    
    if Lista1[i] != Lista2[j]:
        longest = AuxLCS(Lista1, Lista2, i-1, j, r)
        b = AuxLCS(Lista1, Lista2, i, j-1, r)
        if len(longest) < len(b):
            longest = b
    else:
        longest = AuxLCS(Lista1, Lista2, i-1, j-1, r) + [Lista1[i]]
    
    r[i][j] = longest
    return r[i][j]


m = -1

while m<=0:
    m = int(input("Ingrese el numero de elementos en la lista1: "))

Lista1 = []

for i in range(m):
    elemento = input("Ingrese un elemento: ")
    Lista1.append(elemento)

n = -1

while n<=0:
    n = int(input("Ingrese el numero de elementos en la lista2: "))

Lista2 = []

for i in range(n):
    elemento = input("Ingrese un elemento: ")
    Lista2.append(elemento)

subsecuencia = LCS(Lista1, Lista2, m, n)

print(f"La subsecuencia más larga es: {subsecuencia}")