class NodoPila:
    def __init__(self, val):
        self.valor = val
        self.puntero = None

class Pila:
    def __init__(self):
        self.cabeza = None
    
    def push(self, val):
        nodo = NodoPila(val)
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            nodo.puntero = self.cabeza
            self.cabeza = nodo
    
    def pop(self):
        self.cabeza = self.cabeza.puntero
    
    def peek(self):
        paux = self.cabeza
        while paux.puntero != None:
            paux = paux.puntero
        return paux.valor
    
    def isEmpty(self):
        if self.cabeza == None:
            return True
        else:
            return False

print("     Inserte elementos en la pila        ")
print('Si quiere salir diguite "S"')

v = None
pila = Pila()
while v != "S":
    v = input("Ingrese un elemento en la pila: ")
    if(v != "S"):
        pila.push(v)