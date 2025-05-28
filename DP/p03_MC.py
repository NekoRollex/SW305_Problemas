def NCaminos(m, n):
    r = [[None for j in range(n)] for i in range(m)]
    r[0][0] = 1
    return NCaminosAux(m-1, n-1, r)

def NCaminosAux(m, n, r):
    if r[m][n] != None:
        return r[m][n]
    
    if m == 0 or n == 0:
        caminos = 1
    else:
        caminos = NCaminosAux(m-1, n, r) + NCaminosAux(m, n-1, r)
    
    r[m][n] = caminos
    return r[m][n]
    
        

m = -1

while m<=0:
    m = int(input("Ingrese el numero de filas de la matriz: "))

n = -1

while n<=0:
    n = int(input("Ingrese el numero de columnas de la matriz: "))

caminos = NCaminos(m, n)

print(f"El numero de caminos posibles desde (0,0) hasta ({m-1},{n-1}) es: ")
print(caminos)