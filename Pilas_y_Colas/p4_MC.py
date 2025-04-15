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


def invertirOracion(oracion):
        pila = Pila()
        i = 0
        while i != len(oracion):
            pila.push(oracion[i])
            i += 1
        paux = pila.cabeza
        oracionInvertida = ""
        while paux != None:
            oracionInvertida += paux.valor
            paux = paux.puntero
        return oracionInvertida
            
oracion = input("Ingrese una palabra: ")
oracioninvertida = invertirOracion(oracion)

print(oracioninvertida)