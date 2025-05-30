class NodoLista:
    def __init__(self, valor):
        self.valor = valor
        self.punt = None

class ListaEnlazada:
    def __init__(self):
        self.pinicio = None
        self.pfinal = None

    def insertarNodoInicio(self, valor):
        nuevoNodo = NodoLista(valor)
        if self.pinicio is None:
            self.pinicio = nuevoNodo
            self.pfinal = nuevoNodo
        else:
            nuevoNodo.punt = self.pinicio
            self.pinicio = nuevoNodo
    
    def recorrerLista(self):
        actual = self.pinicio
        while actual:
            print(actual.valor, end=" ")
            actual = actual.punt

    
lista = ListaEnlazada() 

print("Agregar elementos ('S' para terminar)")

while True:
    elemento = input("Ingresa el elemento: ")
    if elemento.upper() == 'S':
        break
    lista.insertarNodoInicio(elemento)

lista.recorrerLista()