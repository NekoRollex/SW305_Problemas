class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class ListaEnlazada:
    def __init__(self):
        self.inicio = None
        self.final = None

    def insertarFinal(self, valor):
        nodo = Nodo(valor)
        if self.final is not None:
            self.final.siguiente = nodo
        self.final = nodo
        if self.inicio is None:
            self.inicio = nodo

    def insertarInicio(self, valor):
        nodo = Nodo(valor)
        if self.inicio is not None:
            nodo.siguiente = self.inicio
        self.inicio = nodo
        if self.final is None:
            self.final = nodo
            
    def print(self):
        nodo = self.inicio
        print("Lista enlazada:", end=" ")
        while nodo is not None:
            print(nodo.valor, end=(" -> " if nodo.siguiente is not None else "\n"))
            nodo = nodo.siguiente

    def contarNodos(self):
        contador = 0
        nodo = self.inicio
        while nodo is not None:
            contador += 1
            nodo = nodo.siguiente
        return contador

lista = ListaEnlazada()
print("1. Agregar al inicio")
print("2. Agregar al final")
print("3. Contar nodos")
print("4. Salir")

while True:
    op = input("Ingrese la operación: ")
    if op == "1":
        valor = input("Ingrese el valor a agregar: ")
        lista.insertarInicio(valor)
    elif op == "2":
        valor = input("Ingrese el valor a agregar: ")
        lista.insertarFinal(valor)
    elif op == "3":
        print("Cantidad de nodos:", lista.contarNodos())
    elif op == "4":
        print("Saliendo...")
        break
    else:
        print("Operación no válida")

lista.print()