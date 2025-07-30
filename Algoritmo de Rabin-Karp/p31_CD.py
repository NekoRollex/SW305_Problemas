# 31. Implementación paso a paso
#   Texto: "abracadabra"
#   Patrón: "abra"
#   -	Implementa Rabin-Karp manualmente.
#   -	Muestra cada hash generado por desplazamiento.
#   -	¿En qué posiciones aparece el patrón?

def rabin_karp_simple(texto, patron, base=10, mod=13):
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
        print(f'Hash texto "{texto[i:i + m]}": {hash_texto}')
        if hash_texto == hash_patron:
            if texto[i:i + m] == patron:
                posiciones.append(i)

        if i < n - m:
            hash_texto = (base * (hash_texto - ord(texto[i]) * h) + ord(texto[i + m])) % mod
            if hash_texto < 0:
                hash_texto += mod

    return posiciones


texto = "abracadabra"
patron = "abra"

resultado = rabin_karp_simple(texto, patron)
print("Coincidencias encontradas en las posiciones:", resultado)