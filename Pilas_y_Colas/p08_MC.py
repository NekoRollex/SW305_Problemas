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

print("     Fila en la recepcion        ")
print('Si quiere salir diguite -1')

v = None
cola = Cola()
while v != -1:
    v = int(input("Ingrese el numero del cliente: "))
    if(v != -1):
        cola.enqueque(v)