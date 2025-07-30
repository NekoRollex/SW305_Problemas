def BusquedaNaive(cadena: str , patron: str):
    comparaciones = 0
    posiciones = []
    i = 0
    j = 0
    n1 = len(cadena)
    n2 = len(patron)

    if n1 < n2:
        return None

    while i < n1:
        if cadena[i] == patron[0]:
            k = i
            j = 0
            while (k < n1 and j < n2) and patron[j] == cadena[k]:
                comparaciones += 1
                k += 1
                j += 1
            if j == n2:
                posiciones.append(i)
        else:
            comparaciones += 1
        i += 1
    return posiciones, comparaciones

def LPS(patron: str):
    n = len(patron)
    LPStabla = []
    for i in range(n):
        prefijo = ""
        sufijo = ""
        LPSval = 0
        for j in range(i):
            prefijo += patron[j]
            sufijo = patron[i-j] + sufijo
            if prefijo == sufijo:
                LPSval = j+1
        
        LPStabla.append(LPSval)

    return LPStabla  

def KMP(patron: str, cadena: str):
    resultados = []
    m = len(patron)
    n = len(cadena)
    LPStabla = LPS(patron)
    comparaciones = 0
    j = 0
    i = 0
    while i < n:
        comparaciones += 1       
        if cadena[i] == patron[j]:           
            j +=1

            if j == m:
                resultados.append(i-j+1)
                j = LPStabla[j-1]
            
            i += 1
        else:
            if j>0:
                j = LPStabla[j-1]
            else:
                i += 1

    return resultados, comparaciones

cadena = "AAAAAAAAAAAAAAAAAB"
patron = "AAAAB"

resultados, comparaciones1 = KMP(patron, cadena)
print(f"El patron se encuentra en las posiciones: {resultados}")
print(f"El numero de comparaciones en el KMP es: {comparaciones1}")

posiciones, comparaciones2 = BusquedaNaive(cadena, patron)
print(f"El numero de comparaciones en algoritmo Naive es: {comparaciones2}")