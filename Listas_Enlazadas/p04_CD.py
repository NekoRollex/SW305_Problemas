class NodoLista:
    def __init__ (self,valor):
        self.valor = valor
        self.punt = None
    
class ListaEnlazada:
    def __init__(self):
        self.pinicio = None
        self.pfinal = None
    
    def insertarNodoFinal(self, valor):
        nuevoNodo = NodoLista(valor)
        if self.pinicio is None:
            self.pinicio = nuevoNodo
            self.pfinal = nuevoNodo
        else:
            self.pfinal.punt = nuevoNodo
            self.pfinal = nuevoNodo
    
    def contarNodos(self):
        cont = 0
        actual = self.pinicio
        while actual:
            cont += 1
            actual = actual.punt
        return cont
    
lista = ListaEnlazada() 

print("Agregar elementos ('S' para terminar)")

while True:
    elemento = input("Ingresa el elemento: ")
    if elemento.upper() == 'S':
        break
    lista.insertarNodoFinal(elemento)

print(f"La lista tiene {lista.contarNodos()} nodos")