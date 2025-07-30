def Burbuja(lista):
    n = len(lista)

    i = 0
    while i<n-1:
        j = i+1
        while j<n:
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
            j += 1
        i += 1

def BuscarSuma(lista, suma):
    Copia = lista.copy()
    resultados = []
    listaAux = []
    AuxBuscarSuma(Copia, listaAux, suma, resultados)
    return resultados

def AuxBuscarSuma(lista, listaAux, suma, resultados):
    if lista:
        Copia = lista.copy()
        a = Copia.pop(0)
        listaReAux = listaAux.copy()
        AuxBuscarSuma(Copia, listaReAux, suma, resultados)
        s = 0
        for i in listaAux:
            s += i
        
        if s + a < suma:
            listaAux.append(a)
            AuxBuscarSuma(lista, listaAux, suma, resultados)
        else:
            if s+a == suma:
                listaAux.append(a)
                resultados.append(listaAux)

print("Crear Lista")
print("Si quiere salir ingrese 0")

lista = []

elemento = 1
while elemento != 0:
    elemento = int(input("Ingrese un elemento: "))
    if elemento != 0:
        lista.append(elemento)

Burbuja(lista)
suma = int(input("Ingrese la suma que desea buscar: "))

r = BuscarSuma(lista, suma)
print("Las posibles conbinaciones son: ")
print(r)