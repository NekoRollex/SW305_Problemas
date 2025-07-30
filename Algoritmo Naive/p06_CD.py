# 6. Patrones de longitud 1 o igual al texto
#   Caso A: Texto: "bbbbbbbbbb" | Patrón: "b"
#   Caso B: Texto: "abcde" | Patrón: "abcde"
#   - ¿Cuál es la complejidad en cada caso?
#   -	¿El algoritmo es eficiente en estos extremos?

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

# Caso A
texto_a = "bbbbbbbbbb"
patron_a = "b"
posiciones_a, comp_a = naive_search(texto_a, patron_a)
print(f"Caso A - Patrón longitud 1")
print(f"Posiciones encontradas: {posiciones_a}")
print(f"Comparaciones realizadas: {comp_a}\n")

# Caso B
texto_b = "abcde"
patron_b = "abcde"
posiciones_b, comp_b = naive_search(texto_b, patron_b)
print(f"Caso B - Patrón igual al texto")
print(f"Posiciones encontradas: {posiciones_b}")
print(f"Comparaciones realizadas: {comp_b}")