class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, cliente):
        nodo = NodoCola(cliente)
        if self.back is not None:
            self.back.next = nodo
        self.back = nodo
        if self.front is None:
            self.front = nodo
    
    def dequeue(self):
        if self.front is not None:
            cliente = self.front
            self.front = cliente.next
            if self.front is None:
                self.back = None
            return cliente.valor
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
            print("Cliente ", nodo.valor, end = (" -> " if nodo.next is not None else "\n"))
            nodo = nodo.next


fila = Cola()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)

print("Fila de atención antes de atender a un cliente:")
fila.print()

cliente_atendido = fila.dequeue()
print("Cliente atendido: ", cliente_atendido)

print("Fila de atención después de atender a un cliente:")
fila.print()

cliente_atendido = fila.dequeue()
print("Cliente atendido: ", cliente_atendido)

print("Fila de atención después de atender a otro cliente:")
fila.print()
