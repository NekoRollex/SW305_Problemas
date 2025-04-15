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
        
    def recorrerLista(self):
        paux = self.pinicio
        while paux != None:
            print(paux.valor)
            paux = paux.puntero

    
    def eliminarElemento(self, val):
        esta = False
        paux = self.pinicio
        psiguiente = self.pinicio
        panterior = self.pinicio
        while paux != None and esta==False:
            if paux.valor == val:
                esta = True
            else:
                paux = paux.puntero
        if esta:
            if paux == self.pinicio:
                self.pinicio = self.pinicio.puntero
            elif paux == self.pfinal:
                while panterior.puntero != self.pfinal:
                    panterior = panterior.puntero
                self.pfinal = panterior
                self.pfinal.puntero	= None
            else:
                psiguiente = paux.puntero
                while panterior.puntero != paux:
                    panterior = panterior.puntero
                panterior.puntero = psiguiente

print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v!="S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoFinal(v)

elemento = input("Ingrese el elemento a eliminar: ")

lista.eliminarElemento(elemento)
print("Lista despues de eliminar el elemento")
lista.recorrerLista()