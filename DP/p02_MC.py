def MaxMochila(capacidad, pesos, valores):
    r = [None for i in range(capacidad + 1)]
    return MaxMochilaAux(capacidad, pesos, valores, r)

def MaxMochilaAux(capacidad, pesos, valores, r):
    if r[capacidad] != None:
        return r[capacidad]
    elif capacidad == 0:
        max = 0
    else:
        j = 0
        max = -1
        while j<len(pesos) and pesos[j] <= capacidad:
            a = valores[j] + MaxMochilaAux(capacidad - pesos[j], pesos, valores, r)
            if max<=a:
                max = a
            
            j += 1
        
    r[capacidad] = max
    return max

pesos = [1,3,4,5]
valores = [1,4,5,7]
capacidad = 7

maxval = MaxMochila(capacidad, pesos, valores)
print(f"El valor máximo es: {maxval}")