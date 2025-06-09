# 22. Comparación de eficiencia
#   Texto 1: "AAAAAAAAAAAAAAAAAAAB"
#   Texto 2: "ABCDABCDABCDABCD"
#   Patrón: "ABCD"
#   -	Aplica Boyer-Moore en ambos textos.
#   -	¿En cuál caso realiza más desplazamientos? ¿Por qué?

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


texto1 = "AAAAAAAAAAAAAAAAAAAB"
texto2 = "ABCDABCDABCDABCD"
patron = "ABCD"

print(f'Para el texto 1: "{texto1}":')
boyer_moore_bad_char(texto1, patron)
print(f'Para el texto 2: "{texto2}":')
boyer_moore_bad_char(texto2, patron)