def palindroma(palabra):
    return palabra == palabra[::-1]
texto = "ana y bob fueron a ver radar y kayak en el lago."
texto = texto.lower()

palabras = []
palabra_actual = ""

for caracter in texto:
    if 'a' <= caracter <= 'z':
        palabra_actual += caracter
    else:
        if palabra_actual != "":
            palabras.append(palabra_actual)
            palabra_actual = ""

if palabra_actual != "":
    palabras.append(palabra_actual)

palindromas = []
for palabra in palabras:
    if palindroma(palabra):
        palindromas.append(palabra)

print("Numero de palabras palindromas:", palindromas)

if palindromas:
    mayor = palindromas[0]
    for p in palindromas:
        if len(p) > len(mayor):
            mayor = p
    print("La palabra palíndroma más larga es:", mayor)
else:
    print("No se encontraron palabras palíndromas.")
