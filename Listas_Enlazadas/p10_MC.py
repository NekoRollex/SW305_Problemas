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

def Merge(lista1, lista2):
    listaOrdenada = ListaEnlazada()
    paux1 = lista1.pinicio
    paux2 = lista2.pinicio
    while paux1 != None and paux2 != None:
        if paux1.valor < paux2.valor:
            listaOrdenada.insertarNodoFinal(paux1.valor)
            paux1 = paux1.puntero
        else:
            listaOrdenada.insertarNodoFinal(paux2.valor)
            paux2 = paux2.puntero

    while paux1 != None:
            listaOrdenada.insertarNodoFinal(paux1.valor)
            paux1 = paux1.puntero
    while paux2 != None:
            listaOrdenada.insertarNodoFinal(paux2.valor)
            paux2 = paux2.puntero

    return listaOrdenada

print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa -1")

v = None
lista1 = ListaEnlazada()

while v!=-1:
    v = int(input("Ingrese un elemento: "))
    if v != -1:
        lista1.insertarNodoFinal(v)

lista1.ordenarLista()


print("         Lista enlazada 2         ")
print("Cuando quieras salir ingresa -1")

v = None
lista2 = ListaEnlazada()

while v!=-1:
    v = int(input("Ingrese un elemento: "))
    if v != -1:
        lista2.insertarNodoFinal(v)

lista2.ordenarLista()

lista3 = Merge(lista1, lista2)

print("Lista ordenada, combinada de las 2 listas")

lista3.recorrerLista()