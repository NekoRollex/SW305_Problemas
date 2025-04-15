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
    
    def ordenarLista(self):
        paux1 = self.pinicio        
        while paux1.puntero != None:
            paux2 = paux1.puntero
            while paux2 != None:
                if paux2.valor < paux1.valor:
                    val = paux1.valor
                    paux1.valor = paux2.valor
                    paux2.valor = val
                paux2 = paux2.puntero
            paux1 = paux1.puntero
    
    def recorrerLista(self):
        paux = self.pinicio
        while paux != None:
            print(paux.valor)
            paux = paux.puntero

print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa -1")

v = None
lista = ListaEnlazada()

while v!=-1:
    v = int(input("Ingrese un elemento: "))
    if v != -1:
        lista.insertarNodoFinal(v)

lista.ordenarLista()

print("Lista Ordenada:")

lista.recorrerLista()