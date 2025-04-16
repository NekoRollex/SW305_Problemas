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
    
    def buscar(self,valor):
        actual = self.pinicio
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.punt
        return False
                    
lista = ListaEnlazada() 

print("Agregar elementos ('S' para terminar)")

while True:
    elemento = input("Ingresa el elemento: ")
    if elemento.upper() == 'S':
        break
    lista.insertarNodoFinal(elemento)

valor_buscado = input("¿Que valor se desea buscar?: ")

if lista.buscar(valor_buscado):
    print(f"El valor {valor_buscado} EXISTE en la lista")
else:
    print(f"El valor {valor_buscado} NO EXISTE en la lista")