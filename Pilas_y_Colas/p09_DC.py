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
            if self.front is None:
                self.back = None
            return valor.valor
        return None

    def peek(self):
        if self.front is not None:
            return self.front.valor
        return None

    def is_empty(self):
        return self.front is None

    def print(self):
        nodo = self.front
        while nodo is not None:
            print(nodo.valor, end = (" -> " if nodo.next is not None else "\n"))
            nodo = nodo.next

    def get_size(self):
        size = 0
        nodo = self.front
        while nodo is not None:
            size += 1
            nodo = nodo.next
        return size

cola = Cola()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)

print("Contenido de la cola:")
cola.print()

print("Número de elementos en la cola:", cola.get_size())
