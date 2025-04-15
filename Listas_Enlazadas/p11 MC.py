class NodoLista:
    def __init__(self, val):
        self.valor = val
        self.puntero = None 

class ListaEnlazada:
    def __init__(self):
        self.pfinal = None
        self.pinicio = None
    
    def insertarNodoFinal(self, val):
        nuevoNodo = NodoLista(val)
        if self.pinicio == None:
            self.pinicio = nuevoNodo
            self.pfinal = self.pinicio
            self.pinicio.puntero = self.pfinal
        else:
            self.pfinal.puntero = nuevoNodo
            self.pfinal = self.pfinal.puntero

    def algoritmoTortugaLiebre(self):
        ciclo = False
        tortuga = self.pinicio
        liebre = self.pinicio
        while liebre != None and ciclo == False:
            if liebre.puntero !=None:
                tortuga = tortuga.puntero
                liebre = liebre.puntero
                liebre = liebre.puntero
                if liebre == tortuga:
                    ciclo = True
            else:
                ciclo = False
                return ciclo
        return ciclo            


print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v != "S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoFinal(v)

ciclo = lista.algoritmoTortugaLiebre()

if ciclo:
    print("Hay un ciclo en la lista")
else:
    print("No hay ciclo en la lista")