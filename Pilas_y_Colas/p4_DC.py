class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class Pila:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, valor):
        nodo = NodoPila(valor)
        nodo.next = self.top
        self.top = nodo
        self.size += 1
    
    def pop(self):
        if not self.is_empty():
            nodo = self.top
            self.top = nodo.next
            self.size -= 1
            return nodo.valor
        return None

    def is_empty(self):
        return self.size == 0

def invertir_palabra(palabra):
    pila = Pila()
    
    for letra in palabra:
        pila.push(letra)
    
    palabra_invertida = ""
    while not pila.is_empty():
        palabra_invertida += pila.pop()
    
    return palabra_invertida

palabra = input("Ingrese una palabra: ")
print("Palabra original:", palabra)
palabra_invertida = invertir_palabra(palabra)
print("Palabra invertida:", palabra_invertida)
