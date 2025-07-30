# 1. Búsqueda básica
#   Texto: "abcabcabcdabcde"
#   Patrón: "abcd"
#   -	Aplica manualmente el algoritmo Naive paso a paso.
#   -  	¿Cuántas comparaciones se hacen en total?
#   -	¿En qué posiciones se encuentra el patrón?

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


texto = "abcabcabcdabcde"
patron = "abcd"

posiciones, total_comparaciones = naive_search(texto, patron)

print("Posiciones donde se encuentra el patrón:", posiciones)
print("Total de comparaciones realizadas:", total_comparaciones)