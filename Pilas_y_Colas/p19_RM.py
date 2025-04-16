class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Pila:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nodo = Nodo(valor)
        nodo.siguiente = self.cima
        self.cima = nodo
    
    def pop(self):
        nodo = self.cima
        if not self.is_empty():
            self.cima = nodo.siguiente

    def peek(self):
        if not self.is_empty():
            return self.cima.valor
        return None
            
    def is_empty(self):
        return self.cima is None

class Cola_con_Pilas:
    def __init__(self):
        self.pushStack = Pila()
        self.popStack = Pila()

    def enqueue(self, valor):
        self.pushStack.push(valor)

    def dequeue(self):
        if self.popStack.is_empty():
            while not self.pushStack.is_empty():
                self.popStack.push(self.pushStack.peek())
                self.pushStack.pop()
        self.popStack.pop()

    def peek(self):
        if self.is_empty():
            return None
        if self.popStack.is_empty():
            while not self.pushStack.is_empty():
                self.popStack.push(self.pushStack.peek())
                self.pushStack.pop()
        return self.popStack.peek()

    def is_empty(self):
        return self.pushStack.is_empty() and self.popStack.is_empty()

cola = Cola_con_Pilas()
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