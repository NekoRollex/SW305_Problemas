# 3. Múltiples coincidencias
#   Texto: "aaaabaaabaaabaaaab"
#   Patrón: "aaab"
#   -	Encuentra todas las posiciones de coincidencia.
#   -	¿Qué sucede si haces una optimización con "saltos" cuando hay coincidencia parcial?


# Sin optimizacion
def naive_search(text, patron):
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

# Con optimizacion
def naive_search_optimizado(texto, patron):
    n = len(texto)
    m = len(patron)
    comparaciones = 0
    posiciones = []

    i=0
    while i <= n - m:
        es_igual = True
        for j in range(m):
            comparaciones += 1
            if texto[i + j] != patron[j]:
                es_igual = False
                break
        if es_igual:
            posiciones.append(i)
            i += m
        else:
            i += 1
    
    return posiciones, comparaciones


texto = "aaaabaaabaaabaaaab"
patron = "aaab"

print("Sin optimización:")
posiciones, comparaciones = naive_search(texto, patron)

if posiciones:
    print(f"Posiciones donde se encuentra el patrón: {posiciones}")
else:
    print(f"El patrón no ha sido encontrado")

print("Total de comparaciones realizadas:", comparaciones)


print("\nCon optimización:")
posiciones, comparaciones = naive_search_optimizado(texto, patron)

if posiciones:
    print(f"Posiciones donde se encuentra el patrón: {posiciones}")
else:
    print(f"El patrón no ha sido encontrado")

print("Total de comparaciones realizadas:", comparaciones)