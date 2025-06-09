#texto = input("Ingrese una oracion: ")
texto = "estructura, algoritmo, cadena, texto, análisis"
texto = texto.lower()
texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")\
             .replace("ó", "o").replace("ú", "u")

frecuencia = [0] * 26

for caracter in texto:
    if 'a' <= caracter <= 'z':
        indice = ord(caracter) - ord('a')
        frecuencia[indice] += 1

for i in range(26):
    letra = chr(ord('a') + i)
    print(f"{letra}: {frecuencia[i]}")

max_frecuencia = max(frecuencia)
letra_mas_frecuente = chr(frecuencia.index(max_frecuencia) + ord('a'))
print("\nLetra más frecuente:", letra_mas_frecuente)

print("Letras que no aparecen:")
for i in range(26):
    if frecuencia[i] == 0:
        print(chr(ord('a') + i), end=" ")
