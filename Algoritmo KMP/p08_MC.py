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

patron = "ABABCABAB"

LPStabla = LPS(patron)

print(f"Tabla LPS: {LPStabla}")