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

class Cola_con_dos_prioridades:
    def __init__(self):
        self.colaPrioritaria = Cola()
        self.colaNormal = Cola()

    def enqueue(self, valor, prioridad):
        if prioridad:
            self.colaPrioritaria.enqueue(valor)
        else:
            self.colaNormal.enqueue(valor)

    def dequeue(self):
        if not self.colaPrioritaria.is_empty():
            self.colaPrioritaria.dequeue()
        elif not self.colaNormal.is_empty():
            self.colaNormal.dequeue()

    def peek(self):
        if not self.colaPrioritaria.is_empty():
            return self.colaPrioritaria.peek()
        elif not self.colaNormal.is_empty():
            return self.colaNormal.peek()
        return None
    
    def is_empty(self):
        return self.colaPrioritaria.is_empty() and self.colaNormal.is_empty()

cola = Cola_con_dos_prioridades()
print("1. Agregar al final")
print("2. Eliminar del inicio")
print("3. Ver el inicio")
print("4. Salir")

# Ejemplo propuesto
while True:
    op = input("Ingrese la operación: ")
    if op == "1":
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        cola.enqueue(nombre, edad >= 18)
    elif op == "2":
        cola.dequeue()
    elif op == "3":
        print(cola.peek())
    elif op == "4":
        print("Saliendo...")
        break
    else:
        print("Operación no válida")