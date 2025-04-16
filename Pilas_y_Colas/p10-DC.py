class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, valor):
        nodo = NodoCola(valor)
        if self.back is not None:
            self.back.next = nodo
        self.back = nodo
        if self.front is None:
            self.front = nodo
    
    def dequeue(self):
        if self.front is not None:
            valor = self.front
            self.front = valor.next
            return valor.valor
        return None

    def is_empty(self):
        return self.front is None

    def print(self):
        nodo = self.front
        while nodo:
            print(nodo.valor, end = (" -> " if nodo.next else "\n"))
            nodo = nodo.next

class Pila:
    def __init__(self):
        self.top = None

    def push(self, valor):
        nodo = NodoCola(valor)
        nodo.next = self.top
        self.top = nodo

    def pop(self):
        if self.top:
            valor = self.top
            self.top = valor.next
            return valor.valor
        return None

def invertir_cola(cola):
    pila = Pila()
    
    while not cola.is_empty():
        pila.push(cola.dequeue())

    while pila.top:
        cola.enqueue(pila.pop())

cola = Cola()

cola.enqueue(10)
cola.enqueue(13)
cola.enqueue(50)
cola.enqueue(40)

print("Contenido de la cola antes de invertir:")
cola.print()

invertir_cola(cola)

print("Contenido de la cola después de invertir:")
cola.print()
