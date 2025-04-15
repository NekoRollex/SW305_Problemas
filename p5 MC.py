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
    
    def existeElemento(self, val):
        esta = False
        paux = self.pinicio
        while paux != None and esta==False:
            if paux.valor == val:
                esta = True
            paux = paux.puntero
        return esta


print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v!="S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoFinal(v)

elemento = input("Ingrese el elemento a buscar: ")

esta = lista.existeElemento(elemento)

if esta:
    print("El elemento si se encuentra en la lista")
else:
    print("El elemento no se encuentra en la lista")