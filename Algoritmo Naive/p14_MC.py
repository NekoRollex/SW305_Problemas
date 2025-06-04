def invertircadena(cadena):
    invertido = ""
    n = len(cadena)
    i = n-1
    while 0<=i:
        invertido += cadena[i]
        i -= 1
    
    return invertido

def maslarga(lista):
    palabralarga = ""
    long = -1
    for i in lista:
        if len(i) > long:
            palabralarga = i
            long = len(i)
    
    return long, palabralarga


cadena = input("Ingrese una cadena: ")

lista = []

i = 0

subcadena = ""
letra = False

n = len(cadena)
while i < n:
    if cadena[i] != ' ':
        letra = True
        subcadena += cadena[i]
    else:
        if letra == True:
            inver = invertircadena(subcadena)
            if inver == subcadena:
                lista.append(subcadena)
            subcadena = ""
            letra = False
    i += 1

if letra == True:
    inver = invertircadena(subcadena)
    if inver == subcadena:
        lista.append(subcadena)

longitudmax, palabramax = maslarga(lista)

print(f"La palabra palindorma más larga es {palabramax} y tiene {longitudmax} caracteres")