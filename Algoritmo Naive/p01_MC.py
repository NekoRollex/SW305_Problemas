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
                i = k-1
        else:
            comparaciones += 1
        i += 1
    return posiciones, comparaciones


cadena = "abcabcabcdabcde"
patron = "abcd"

posiciones, comparaciones = BusquedaNaive(cadena, patron)

print(f"El patron se encuentra en las posiciones: {posiciones}")
print(f"El numero de comparaciones realizadas es: {comparaciones}")