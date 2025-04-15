class NodoLista:
    def __init__(self, val):
        self.valor = val
        self.puntero = None 

class ListaEnlazada:
    def __init__(self):
        self.pfinal = None
        self.pinicio = None
    
    def insertarNodoFinal(self, val):
        nuevoNodo = NodoLista(val)
        if self.pinicio == None:
            self.pinicio = nuevoNodo
            self.pfinal = self.pinicio
            self.pinicio.puntero = self.pfinal
        else:
            self.pfinal.puntero = nuevoNodo
            self.pfinal = self.pfinal.puntero

    def nElementos(self):
        n = 0
        paux = self.pinicio
        while paux != None:
            n += 1
            paux = paux.puntero
        return n
    
    def elementoMedio(self):
        n = self.nElementos()
        medio = n//2
        paux = self.pinicio
        i = 0
        while i != medio:
            paux = paux.puntero
            i += 1
        return paux.valor

print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v != "S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoFinal(v)

n = lista.nElementos()

if n%2 == 0:
    print(f"Se ha considerado el elemento medio como el elemento con indice {n/2}")

valor = lista.elementoMedio()
print(f"El valor medio es: {valor}")