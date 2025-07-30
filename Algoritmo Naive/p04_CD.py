# 4. Conteo de apariciones
#   Texto: "ababababab"
#   Patrón: "abab"
#   -	Usa el algoritmo Naive para contar cuántas veces aparece el patrón.
#   - 	¿Qué posiciones devuelven coincidencias superpuestas?

def naive_search(texto, patron):
    n = len(texto)
    m = len(patron)
    posiciones = []

    for i in range(n - m + 1):
        if texto[i:i + m] == patron:
            posiciones.append(i)

    return posiciones


texto = "ababababab"
patron = "abab"

posiciones = naive_search(texto, patron)

print("Coincidencias encontradas en posiciones:", posiciones)
print("Total de apariciones:", len(posiciones))

superpuestas = [pos for i, pos in enumerate(posiciones[1:], 1) if pos < posiciones[i - 1] + len(patron)]
print("Coincidencias superpuestas en posiciones:", superpuestas)