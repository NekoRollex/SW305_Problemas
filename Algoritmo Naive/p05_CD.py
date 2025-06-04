# 5. Emparejamiento en cadenas de ADN
#   Texto (ADN): "AGCTTAGCTTAGCTAAGCTT"
#   Patrón: "AGCTT"
#   -	Encuentra todas las apariciones exactas del patrón.
#   -	¿Cuántas comparaciones se hacen?

def naive_search(texto, patron):
    n = len(texto)
    m = len(patron)
    posiciones = []
    total_comparaciones = 0

    for i in range(n - m + 1):
        print(f"Pos {i}: '{texto[i:i + m]}' vs '{patron}'", end=' — ')

        es_igual = True
        comparaciones_antes = total_comparaciones

        for j in range(m):
            total_comparaciones += 1
            if texto[i + j] != patron[j]:
                es_igual = False
                break

        comparaciones_hechas = total_comparaciones - comparaciones_antes
        print(f"Comparaciones acumuladas: {total_comparaciones} (+{comparaciones_hechas})")

        if es_igual:
            posiciones.append(i)

    return posiciones, total_comparaciones


texto = "AGCTTAGCTTAGCTAAGCTT"
patron = "AGCTT"

posiciones, total = naive_search(texto, patron)
print("\nCoincidencias encontradas en posiciones:", posiciones)
print("Total comparaciones realizadas:", total)