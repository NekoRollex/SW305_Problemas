#30. Comparación con fuerza bruta
#   Texto: "ABCDEFABCDEF"
#   Patrón: "DEF"
#   -	Cuenta el número de comparaciones usando el algoritmo Naive.
#   -	Luego usa Rabin-Karp con base 256 y mod 101.
#   -	Compara ambos métodos en eficiencia.

# Algoritmo Naive
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


# Rabin-Karp
def rabin_karp_simple(texto, patron, base=256, mod=101):
    n = len(texto)
    m = len(patron)
    h = pow(base, m - 1, mod)
    hash_patron = 0
    hash_texto = 0
    posiciones = []
    comparaciones = 0

    for i in range(m):
        hash_patron = (base * hash_patron + ord(patron[i])) % mod
        hash_texto = (base * hash_texto + ord(texto[i])) % mod

    print(f"Hash del patrón '{patron}': {hash_patron}")

    for i in range(n - m + 1):
        if hash_texto == hash_patron:
            es_igual = True
            for j in range(m):
                comparaciones += 1
                if texto[i + j] != patron[j]:
                    es_igual = False
                    break
            if es_igual:
                posiciones.append(i)

        if i < n - m:
            hash_texto = (base * (hash_texto - ord(texto[i]) * h) + ord(texto[i + m])) % mod
            if hash_texto < 0:
                hash_texto += mod

    return posiciones, comparaciones


texto = "ABCDEFABCDEF"
patron = "DEF"

print("Algoritmo Naive:")
pos_naive, comp_naive = naive_search(texto, patron)
print("Coincidencias encontradas en las posiciones:", pos_naive)
print("Total de comparaciones:", comp_naive)

print("Algoritmo Rabin-Karp:")
pos_rabin_karp, comp_rabin_karp = rabin_karp_simple(texto, patron)
print("Coincidencias encontradas en las posiciones:", pos_rabin_karp)
print("Total de comparaciones:", comp_rabin_karp)