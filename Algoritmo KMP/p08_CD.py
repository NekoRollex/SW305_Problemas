# 8. Construcción de la tabla LPS (Longest Prefix Suffix)
#   Patrón: "ABABCABAB"
#   -	Construye paso a paso la tabla LPS.
#   -	¿Qué representa cada valor en la tabla?
#   -	¿Qué observas en relación con los prefijos y sufijos del patrón?

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


patron = "ABABCABAB"
tabla_lps = construir_lps(patron)

print("Patrón: ", patron)
print("Tabla LPS:", tabla_lps)