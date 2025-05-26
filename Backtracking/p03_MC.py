def posiblesPermutaciones(lista):
    permutaciones = []
    listaaux = []
    auxPermutaciones(lista, permutaciones, listaaux)
    return permutaciones

def auxPermutaciones(lista, permutaciones, listaaux):
    n = len(lista)
    if n > 1:
        for i in range(n):
            a = lista.pop(i)
            g = list(listaaux)
            listaaux.append(a)
            auxPermutaciones(lista, permutaciones, listaaux)
            lista.insert(i, a)
            listaaux = g
    else:
        listaaux.append(lista[0])
        permutaciones.append(listaaux)

print("Crear Lista")
print("Si quiere salir ingrese 0")

lista = []

elemento = 1
while elemento != 0:
    elemento = int(input("Ingrese un elemento: "))
    if elemento != 0:
        lista.append(elemento)

permutaciones = posiblesPermutaciones(lista)

print(f"Las posibles permutaciones son: {permutaciones}")