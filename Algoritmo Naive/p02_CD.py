# 2. Comparación con patrón ausente
#   Texto: "abcdefghijklmnop"
#   Patrón: "xyz"
#   - ¿Qué ocurre si el patrón no existe en el texto?
#   - ¿Cuántas comparaciones se realizan en total?

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


texto = "abcdefghijklmnop"
patron = "xyz"

posiciones, total_comparaciones = naive_search(texto, patron)

if posiciones:
    print(f"Posiciones donde se encuentra el patrón: {posiciones}")
else:
    print(f"El patrón no ha sido encontrado")

print("Total de comparaciones realizadas:", total_comparaciones)