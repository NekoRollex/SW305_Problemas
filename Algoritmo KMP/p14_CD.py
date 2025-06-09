# 14. Caso límite – patrón igual al texto
#   Texto y patrón: "KMPMATCH"
#   -	Construye su LPS.
#   -	¿Qué se espera como resultado del algoritmo?

def construir_lps(patron):
    tabla_lps = [0] * len(patron)
    longitud = 0
    i = 1

    while i < len(patron):
        if patron[i] == patron[longitud]:
            longitud += 1
            tabla_lps[i] = longitud
            i += 1
        else:
            if longitud != 0:
                longitud = tabla_lps[longitud - 1]
            else:
                tabla_lps[i] = 0
                i += 1
    return tabla_lps

def kmp_search(texto, patron):
    tabla_lps = construir_lps(patron)
    i = 0
    j = 0
    posiciones = []
    comparaciones = 0
    while i < len(texto):
        comparaciones += 1
        if texto[i] == patron[j]:
            i += 1
            j += 1
            if j == len(patron):
                posiciones.append(i - j)
                j = tabla_lps[j - 1]
        else:
            if j != 0:
                j = tabla_lps[j - 1]
            else:
                i += 1
    return posiciones, comparaciones, tabla_lps


texto = "KMPMATCH"
patron = "KMPMATCH"

posiciones, total_comparaciones, tabla_lps = kmp_search(texto, patron)

print("Tabla LPS:", tabla_lps)
print("Posiciones encontradas:", posiciones)
print("Número total de comparaciones:", total_comparaciones)