letras = "abcdefghijklmnñopqrstuvwxyz"

frecuencia = [0] * len(letras)

#oracion = input("Ingresa una oración: ")
oracion = "estructura, algoritmo, cadena, texto, análisis"
oracion.lower()
oracion = oracion.replace("á", "a").replace("é", "e").replace("í", "i")\
             .replace("ó", "o").replace("ú", "u")

for caracter in oracion:
    if caracter in letras:
        indice = letras.index(caracter)
        frecuencia[indice] += 1

print("\nFrecuencia de letras:")
for i in range(len(letras)):
    print(f"{letras[i]}: {frecuencia[i]}")

max_frec = max(frecuencia)
letras_frecuentes = []
for i in range(len(frecuencia)):
    if frecuencia[i] == max_frec:
        letras_frecuentes.append(letras[i])

print("\nLetras más frecuentes:", ", ".join(letras_frecuentes))
print("Frecuencia:", max_frec)


print("Letras que no aparecen:")
for i in range(len(letras)):
    if frecuencia[i] == 0:
        print(letras[i], end=" ")
print()
