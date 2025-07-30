# 32. Sensibilidad al cambio de base y módulo
#   Texto: "banana"
#   Patrón: "ana"
#	Prueba con base 256, mod 101.
#	Luego con base 10, mod 13.
#	¿El número de colisiones cambia? ¿Qué conclusión puedes sacar?

def rabin_karp_simple(texto, patron, base, mod):
    n = len(texto)
    m = len(patron)
    h = pow(base, m - 1, mod)
    hash_patron = 0
    hash_texto = 0
    posiciones = []
    colisiones = 0

    for i in range(m):
        hash_patron = (base * hash_patron + ord(patron[i])) % mod
        hash_texto = (base * hash_texto + ord(texto[i])) % mod

    print(f"Hash del patrón '{patron}': {hash_patron}")

    for i in range(n - m + 1):
        if hash_texto == hash_patron:
            if texto[i:i + m] == patron:
                posiciones.append(i)
            else:
                colisiones += 1

        if i < n - m:
            hash_texto = (base * (hash_texto - ord(texto[i]) * h) + ord(texto[i + m])) % mod
            if hash_texto < 0:
                hash_texto += mod

    return posiciones, colisiones


texto = "banana"
patron = "ana"
base = 256
mod = 101

print("base=256 y mod=101:")
resultado, colisiones = rabin_karp_simple(texto, patron, base, mod)
print("Coincidencias encontradas en las posiciones:", resultado)
print("Colisiones:", colisiones)

base = 10
mod = 13

print("base=10 y mod=13:")
resultado, colisiones = rabin_karp_simple(texto, patron, base, mod)
print("Coincidencias encontradas en las posiciones:", resultado)
print("Colisiones:", colisiones)