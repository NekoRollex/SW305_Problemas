# 21. Construcción de la tabla de sufijo bueno
#   Patrón: "ABCDABD"
#   -	Determina las longitudes de los sufijos buenos para cada posición del patrón.
#   -	¿Cómo afecta esto los saltos durante la búsqueda?

def construir_tabla_sufijo_bueno(patron):
    m = len(patron)
    sufijos = [0] * m
    sufijos[m-1] = m
    k = m - 1
    j = 0
    for i in range(m-2, -1, -1):
        if i > k and sufijos[i + m - 1 - j] < i - k:
            sufijos[i] = sufijos[i + m - 1 - j]
        else:
            k = i
            j = i
            while k >= 0 and patron[k] == patron[k + m - 1 - j]:
                k -= 1
            sufijos[i] = j - k
    return sufijos


patron = "ABCDABD"
sufijos = construir_tabla_sufijo_bueno(patron)
print("Longitudes de sufijos para cada posición:")
for i, val in enumerate(sufijos):
    print(f"Posición {i}: {val}")