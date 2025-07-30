# 29. Emparejamiento en secuencias de ADN
#   Texto ADN: "GATTACAGATTACA"
#   Patrón: "TACA"
#   -	Calcula hashes para todas las subcadenas de igual longitud.
#   -	¿Cuántas coincidencias exactas hay?
#   -	¿Qué ventaja tiene Rabin-Karp en textos biológicos repetitivos?

def rabin_karp_simple(texto, patron, base=10, mod=13):
    n = len(texto)
    m = len(patron)
    h = pow(base, m - 1, mod)
    hash_patron = 0
    hash_texto = 0
    posiciones = []
    coincidencias = 0
    colisiones = 0

    for i in range(m):
        hash_patron = (base * hash_patron + ord(patron[i])) % mod
        hash_texto = (base * hash_texto + ord(texto[i])) % mod

    print(f"Hash del patrón '{patron}': {hash_patron}")

    for i in range(n - m + 1):
        print(f'Hash texto "{texto[i:i + m]}": {hash_texto}')
        if hash_texto == hash_patron:
            print("Hash coincidente")
            if texto[i:i + m] == patron:
                coincidencias += 1
                posiciones.append(i)
            else:
                colisiones += 1

        if i < n - m:
            hash_texto = (base * (hash_texto - ord(texto[i]) * h) + ord(texto[i + m])) % mod
            if hash_texto < 0:
                hash_texto += mod

    return posiciones, coincidencias, colisiones


texto = "GATTACAGATTACA"
patron = "TACA"

resultado, coincidencias, colisiones = rabin_karp_simple(texto, patron)
print("Coincidencias encontradas en las posiciones:", resultado)
print("Coincidencias exactas encontradas:", coincidencias)
print("Colisiones encontradas:", colisiones)