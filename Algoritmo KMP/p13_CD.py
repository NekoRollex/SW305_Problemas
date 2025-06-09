# 13. KMP en detección de plagio parcial
#   Texto A: "La computación es fascinante porque permite simular el pensamiento humano"
#   Texto B: "El pensamiento humano es fascinante y puede ser simulado por la computación"
#   -	Divide ambos textos en frases de 4 palabras.
#   -	Usa KMP para buscar coincidencias exactas entre los fragmentos.
#   -	¿Qué frases coinciden y cuántas?

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

def subfrases_de_cuatro(texto):
    palabras = texto.split()
    return [palabras[i:i+4] for i in range(len(palabras) - 3)]


texto_A = "La computación es fascinante porque permite simular el pensamiento humano"
texto_B = "El pensamiento humano es fascinante y puede ser simulado por la computación"

frases_A = subfrases_de_cuatro(texto_A)
palabras_B = texto_B.split()

coincidencias = []
total_comparaciones = 0

for frase in frases_A:
    posiciones, comparaciones = kmp_search(palabras_B, frase)
    total_comparaciones += comparaciones
    if posiciones:
        coincidencias.append(' '.join(frase))

if coincidencias:
    print("Frases de 4 palabras de Texto A que aparecen en Texto B:\n")
    for c in coincidencias:
        print(f" - {c}")
    print(f"\nTotal de frases coincidentes: {len(coincidencias)}")
else:
    print("No se encontraron frases de 4 palabras de Texto A en Texto B")

print(f"Total de comparaciones hechas en todas las búsquedas: {total_comparaciones}")