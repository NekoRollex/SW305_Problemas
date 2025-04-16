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
    
cola = Cola()
print(f"Cola vacia: {cola.items}")

cola.enqueue("Juan")
cola.enqueue("1")
cola.enqueue(True)

print(f"Cola actual: {cola.items}")

cola.dequeue()
cola.dequeue()

print("Cola actual:", cola.items)