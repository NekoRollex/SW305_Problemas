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
    
def invertirPalabra(palabra):
    pila = Pila()

    for letra in palabra:
        pila.push(letra)

    invertida = ""
    
    while not pila.is_empty():
        invertida += pila.pop()
    
    return invertida

palabra = "Hola"
invertida = invertirPalabra(palabra)

print(f"Palabra original: {palabra}")
print(f"Palabra invertida: {invertida}")