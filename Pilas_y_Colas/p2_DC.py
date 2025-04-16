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
    
    def print(self):
        nodo = self.top
        while nodo is not None:
            print(nodo.valor, end = (" -> " if nodo.next is not None else "\n"))
            nodo = nodo.next

p= Pila()
print("Ingrese elementos a la pila. Escriba 'fin' para terminar.")
while True:
    val = input("Ingrese un valor: ")
    if val.lower() == 'fin':
        break
    p.push(int(val))
print("Contenido de la pila: ")
p.print()
