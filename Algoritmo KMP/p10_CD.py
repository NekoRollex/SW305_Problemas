# 10. Comparación con Naive
#   Texto: "AAAAAAAAAAAAAAAAAB"
#   Patrón: "AAAAB"
#   -	Aplica el algoritmo Naive y cuenta las comparaciones.
#   -	Aplica KMP y cuenta nuevamente.
#   -	¿Qué tan significativa es la diferencia en eficiencia?

# Algoritmo Naive
def naive_search(texto, patron):
    n = len(texto)
    m = len(patron)
    comparaciones = 0
    posiciones = []

    for i in range(n - m + 1):
        es_igual = True
        for j in range(m):
            comparaciones += 1
            if texto[i + j] != patron[j]:
                es_igual = False
                break
        if es_igual:
            posiciones.append(i)
    
    return posiciones, comparaciones


# Algoritmo KMP
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
    return posiciones, comparaciones


texto = "AAAAAAAAAAAAAAAAAB"
patron = "AAAAB"

# Buscar con Naive
pos_naive, comp_naive = naive_search(texto, patron)
print("Búsqueda Naive:")
print("-Posiciones encontradas:", pos_naive if pos_naive else "No encontrado")
print("-Comparaciones realizadas:", comp_naive)

# Buscar con KMP
pos_kmp, comp_kmp = kmp_search(texto, patron)
print("\nBúsqueda KMP:")
print("-Posiciones encontradas:", pos_kmp if pos_kmp else "No encontrado")
print("-Comparaciones realizadas:", comp_kmp)