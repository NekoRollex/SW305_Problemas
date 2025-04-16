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
            nodo = self.front
            self.front = nodo.next
            if self.front is None:
                self.back = None
            return nodo.valor
        return None
    
    def is_empty(self):
        return self.front is None

    def print(self):
        nodo = self.front
        while nodo is not None:
            print(nodo.valor, end=" -> " if nodo.next is not None else "\n")
            nodo = nodo.next

def fusionar_colas(cola1, cola2):
    cola_fusionada = Cola()

    while not cola1.is_empty() and not cola2.is_empty():
        cola_fusionada.enqueue(cola1.dequeue())
        cola_fusionada.enqueue(cola2.dequeue())

    while not cola1.is_empty():
        cola_fusionada.enqueue(cola1.dequeue())

    while not cola2.is_empty():
        cola_fusionada.enqueue(cola2.dequeue())

    return cola_fusionada

cola1 = Cola()
cola2 = Cola()

cola1.enqueue(1)
cola1.enqueue(6)
cola1.enqueue(7)
cola1.enqueue(10)
cola1.enqueue(13)

cola2.enqueue(2)
cola2.enqueue(4)
cola2.enqueue(6)

print("Cola 1:")
cola1.print()

print("\nCola 2:")
cola2.print()

cola_fusionada = fusionar_colas(cola1, cola2)

print("\nCola Fusionada:")
cola_fusionada.print()
