# 27. Búsqueda exacta con hash simple
#   Texto: "GEEKS FOR GEEKS"
#   Patrón: "GEEK"
#   -	Usa un hash base 256 y módulo 101.
#   -	Calcula el hash del patrón.
#   -	Desliza sobre el texto y encuentra las posiciones de coincidencia.

def rabin_karp_simple(texto, patron, base=256, mod=101):
    n = len(texto)
    m = len(patron)
    h = pow(base, m - 1, mod)
    hash_patron = 0
    hash_texto = 0
    posiciones = []

    for i in range(m):
        hash_patron = (base * hash_patron + ord(patron[i])) % mod
        hash_texto = (base * hash_texto + ord(texto[i])) % mod

    print(f"Hash del patrón '{patron}': {hash_patron}")

    for i in range(n - m + 1):
        if hash_texto == hash_patron:
            if texto[i:i + m] == patron:
                posiciones.append(i)

        if i < n - m:
            hash_texto = (base * (hash_texto - ord(texto[i]) * h) + ord(texto[i + m])) % mod
            if hash_texto < 0:
                hash_texto += mod

    return posiciones


texto = "GEEKS FOR GEEKS"
patron = "GEEK"

resultado = rabin_karp_simple(texto, patron)
print("Coincidencias encontradas en las posiciones:", resultado)