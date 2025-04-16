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

def fusionarColas(cola1, cola2):
    cola3 = Cola()

    while not cola1.is_empty() or not cola2.is_empty():
        if not cola1.is_empty():
            cola3.enqueue(cola1.peek())
            cola1.dequeue()
        if not cola2.is_empty():
            cola3.enqueue(cola2.peek())
            cola2.dequeue()
            
    return cola3

cola1 = Cola()
cola2 = Cola()
print("1. Agregar al final")
print("2. Eliminar del inicio")
print("3. Ver el inicio")
print("4. Salir")

print("\nPrimera Cola")
while True:
    op = input("Ingrese la operación: ")
    if op == "1":
        valor = input("Ingrese el valor a agregar: ")
        cola1.enqueue(valor)
    elif op == "2":
        cola1.dequeue()
    elif op == "3":
        print(cola1.peek())
    elif op == "4":
        print("Saliendo...")
        break
    else:
        print("Operación no válida")

print("\nSegunda Cola")
while True:
    op = input("Ingrese la operación: ")
    if op == "1":
        valor = input("Ingrese el valor a agregar: ")
        cola2.enqueue(valor)
    elif op == "2":
        cola2.dequeue()
    elif op == "3":
        print(cola2.peek())
    elif op == "4":
        print("Saliendo...")
        break
    else:
        print("Operación no válida")

cola1.print()
cola2.print()

cola12 = fusionarColas(cola1, cola2)

print("\nCola fusionada")
cola12.print()