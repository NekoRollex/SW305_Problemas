class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, valor):
        self.items.append(valor)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0
    
fila = Cola()
fila.enqueue("Cliente 1")
fila.enqueue("Cliente 2")
fila.enqueue("Cliente 3")
fila.enqueue("Cliente 4")
fila.enqueue("Cliente 5")

while not fila.is_empty():
    cliente = fila.dequeue()
    print(f"Atendiendo a {cliente}...")

    if not fila.is_empty():
        print(f"Siguiente cliente: {fila.peek()}")
    else:
        print("Ya no quedan mas clientes en la fila")