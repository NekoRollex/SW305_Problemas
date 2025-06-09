# 23. Texto con símbolos especiales
#   Texto: "El correo es info@ejemplo.com y el respaldo está en backup@ejemplo.org"
#   Patrón: "@ejemplo"
#   -	Aplica Boyer-Moore para encontrar todas las apariciones.
#   -	¿Qué tan útil es el algoritmo en cadenas con símbolos no alfabéticos?

def heuristica_caracter_malo(patron):
    bad_char = {}
    for i, c in enumerate(patron):
        bad_char[c] = i
    return bad_char

def boyer_moore_bad_char(texto, patron):
    bad_char = heuristica_caracter_malo(patron)
    n = len(texto)
    m = len(patron)
    s = 0
    comparaciones = 0
    posiciones = []

    while s <= n - m:
        j = m - 1

        while j >= 0 and patron[j] == texto[s + j]:
            comparaciones += 1
            j -= 1

        if j < 0:
            posiciones.append(s)
            s += (m - bad_char.get(texto[s + m], -1)) if s + m < n else 1
        else:
            comparaciones += 1
            bad_char_shift = bad_char.get(texto[s + j], -1)
            shift = max(1, j - bad_char_shift)
            s += shift

    print(f"\nTotal de comparaciones realizadas: {comparaciones}")
    print(f"Posiciones donde se encontró el patrón: {posiciones}")


texto = "El correo es info@ejemplo.com y el respaldo está en backup@ejemplo.org"
patron = "@ejemplo"

boyer_moore_bad_char(texto, patron)