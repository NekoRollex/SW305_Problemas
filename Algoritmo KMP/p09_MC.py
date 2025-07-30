def LPS(patron: str):
    n = len(patron)
    LPStabla = []
    for i in range(n):
        prefijo = ""
        sufijo = ""
        LPSval = 0
        for j in range(i):
            prefijo += patron[j]
            sufijo = patron[i-j] + sufijo
            if prefijo == sufijo:
                LPSval = j+1
        
        LPStabla.append(LPSval)

    return LPStabla  

def KMP(patron: str, cadena: str):
    resultados = []
    m = len(patron)
    n = len(cadena)
    LPStabla = LPS(patron)
    comparaciones = 0
    j = 0
    i = 0
    while i < n:
        comparaciones += 1       
        if cadena[i] == patron[j]:           
            j +=1

            if j == m:
                resultados.append(i-j+1)
                j = LPStabla[j-1]
            
            i += 1
        else:
            if j>0:
                j = LPStabla[j-1]
            else:
                i += 1

    return resultados, comparaciones

cadena = "ABABDABACDABABCABAB"
patron = "ABABCABAB"

resultados, comparaciones = KMP(patron, cadena)
print(f"El patron se encuentra en las posiciones: {resultados}")
print(f"El numero de comparaciones es: {comparaciones}")