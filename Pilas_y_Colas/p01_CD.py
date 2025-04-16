class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Algo salio mal")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


pila = Pila()
pila.push(34)
pila.push(45)
pila.push(56)

print(f"Elemento en el tope: {pila.peek()}")
print(f"Elemento eliminado: {pila.pop()}")
print(f"Nuevo tope: {pila.peek()}")

try:
    print(f"Elemento eliminado: {pila.pop()}")
    print(f"Elemento eliminado: {pila.pop()}")
    print(f"Elemento eliminado: {pila.pop()}")
except IndexError as e:
    print(f"Error: {e}")