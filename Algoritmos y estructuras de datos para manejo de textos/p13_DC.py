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
indice_max = frecuencia.index(max_frec)
print("\nLetra mas frecuente:", letras[indice_max])

print("Letras que no aparecen:")
for i in range(len(letras)):
    if frecuencia[i] == 0:
        print(letras[i], end=" ")
