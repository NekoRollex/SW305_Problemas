class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Cola:
    def __init__(self):
        self.inicio = None
        self.final = None

    def enqueue(self, valor):
        nodo = Nodo(valor)
        if self.final is not None:
            self.final.siguiente = nodo
        self.final = nodo
        if self.inicio is None:
            self.inicio = nodo
    
    def dequeue(self):
        nodo = self.inicio
        if nodo is not None:
            self.inicio = nodo.siguiente

    def peek(self):
        if self.inicio is not None:
            return self.inicio.valor
        return None
            
    def is_empty(self):
        return self.inicio is None

    def print(self):
        nodo = self.inicio
        while nodo is not None:
            print(nodo.valor, end=(" -> " if nodo.siguiente is not None else "\n"))
            nodo = nodo.siguiente

    def clear(self):
        while not self.is_empty():
            self.pop()

cola = Cola()
print("1. Agregar al final")
print("2. Eliminar del inicio")
print("3. Ver el inicio")
print("4. Salir")

while True:
    op = input("Ingrese la operación: ")
    if op == "1":
        valor = input("Ingrese el valor a agregar: ")
        cola.enqueue(valor)
    elif op == "2":
        cola.dequeue()
    elif op == "3":
        print(cola.peek())
    elif op == "4":
        print("Saliendo...")
        break
    else:
        print("Operación no válida")

cola.print()