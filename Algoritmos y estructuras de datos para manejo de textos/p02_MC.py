def BusquedaNaive(cadena: str , patron: str):
    nveces = 0
    i = 0
    j = 0
    n1 = len(cadena)
    n2 = len(patron)

    while i < n1:
        if cadena[i] == patron[0]:
            k = i
            j = 0
            while (k < n1 and j < n2) and patron[j] == cadena[k]:
                k += 1
                j += 1
            if j == n2:
                nveces += 1
        i += 1
    return nveces


cadena = "ATCGATCGAATCG"
patron = "ATCG"

nveces = BusquedaNaive(cadena, patron)

print(f"El patron aparece {nveces} en la cadena")
