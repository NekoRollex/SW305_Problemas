class NodoLista:
    def __init__(self, val):
        self.valor = val
        self.puntero = None 

class ListaEnlazada:
    def __init__(self):
        self.pinicio = None
    
    def insertarNodoInicio(self, val):
        nuevoNodo = NodoLista(val)
        nuevoNodo.puntero = self.pinicio
        self.pinicio = nuevoNodo


print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v!="S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoInicio(v)

paux = lista.pinicio
while paux != None:
    print(paux.valor)
    paux = paux.puntero