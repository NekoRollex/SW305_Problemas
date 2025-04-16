class NodoPila:
    def __init__(self, val):
        self.valor = val
        self.puntero = None

class Cola:
    def __init__(self):
        self.pinicio = None
        self.pfinal = None
    
    def enqueque(self, val):
        if self.pinicio == None:
            nodo = NodoPila(val)
            self.pinicio = nodo
            self.pfinal = self.pinicio
            self.pinicio.puntero = self.pfinal
        else:
            nodo = NodoPila(val)
            self.pfinal.puntero = nodo
            self.pfinal = self.pfinal.puntero
    
    def dequeque(self):
        self.pinicio = self.pinicio.puntero
    
    def peek(self):
        return self.pinicio
    
    def isEmpty(self):
        if self.pinicio == None:
            return True
        else:
            return False

print("     Inserte elementos en la cola        ")
print('Si quiere salir diguite "S"')

v = None
cola = Cola()
while v != "S":
    v = input("Ingrese un elemento en la cola: ")
    if(v != "S"):
        cola.enqueque(v)
