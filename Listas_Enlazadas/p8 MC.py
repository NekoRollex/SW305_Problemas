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
    
    def invertirLista(self):
        paux = self.pinicio
        ListaInvertida = ListaEnlazada()
        while paux != None:
            nuevoNodo = NodoLista(paux.valor)
            nuevoNodo.puntero = ListaInvertida.pinicio
            ListaInvertida.pinicio = nuevoNodo
            paux = paux.puntero
        return ListaInvertida
    
    def recorrerLista(self):
        paux = self.pinicio
        while paux != None:
            print(paux.valor)
            paux = paux.puntero

print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v!="S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoFinal(v)

lista = lista.invertirLista()
print("Nueva Lista:")
lista.recorrerLista()