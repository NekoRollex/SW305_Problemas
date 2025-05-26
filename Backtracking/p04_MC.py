def NReynas(n):
    conjuntoSoluciones = []
    solucion = [None for j in range (n)]

    AuxReynas(solucion, 0, conjuntoSoluciones, n)
    return conjuntoSoluciones

def AuxReynas(solucion, j, conjuntoSoluciones, n):
    for i in range(n):
        if j > 0:
            posible = True
            k = 0
            while (k<j and posible == True):
                if solucion[k] == i:
                    posible = False
                k += 1
            k = 1
            while ((k<=i and k<=j) and posible == True):
                if solucion[j-k] == i-k:
                    posible = False
                k += 1
            
            k = 1
            while ((k <= i and k <= j) and posible == True):
                if solucion[j-k] == i+k:
                    posible = False
                k += 1            
            
            if posible == True:
                solucion[j] = i
                solucionaux = list(solucion)
                if j<n-1:
                    AuxReynas(solucionaux, j+1, conjuntoSoluciones, n)
                else:
                    conjuntoSoluciones.append(solucionaux)
        else:
            solucion[j] = i
            solucionaux = list(solucion)
            AuxReynas(solucionaux, j+1, conjuntoSoluciones, n)           


print("Problema N reinas")

n = -1

while not (n>0):
    n = int(input("Ingrese el numero de filas y columnas del tablero: "))

conj = NReynas(n)
print("El conjunto de las soluciones: ")
print(conj)