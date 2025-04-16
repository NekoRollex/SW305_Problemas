class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, valor):
        nodo = NodoCola(valor)
        if self.back is not None:
            self.back.next = nodo
        self.back = nodo
        self.size += 1
        if self.front is None:
            self.front = nodo
    
    def dequeue(self):
        if self.front is not None:
            nodo = self.front
            self.front = nodo.next
            self.size -= 1
            if self.front is None:
                self.back = None
            return nodo.valor
        return None

cola = Cola()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

print("Elemento eliminado:", cola.dequeue())
