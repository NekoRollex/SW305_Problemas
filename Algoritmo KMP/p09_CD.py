# 9. Aplicación del algoritmo KMP
#   Texto: "ABABDABACDABABCABAB"
#   Patrón: "ABABCABAB"
#   -	Usa la tabla LPS del Ejercicio 1.
#   -	Aplica KMP para encontrar la(s) posición(es) del patrón en el texto.
#   -	¿Cuántas comparaciones se hicieron?

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
    print("Comparaciones:")
    while i < len(texto):
        comparaciones += 1
        print(f"{comparaciones}: texto[{i}]='{texto[i]}' con patron[{j}]='{patron[j]}'")

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


texto = "ABABDABACDABABCABAB"
patron = "ABABCABAB"

posiciones, total_comparaciones = kmp_search(texto, patron)

print("Posiciones encontradas:", posiciones)
print("Número total de comparaciones:", total_comparaciones)