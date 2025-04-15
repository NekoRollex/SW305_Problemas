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

    def nElementos(self):
        n = 0
        paux = self.pinicio
        while paux != None:
            n += 1
            paux = paux.puntero
        return n
    
    def insertarElemento(self, val, indice):
        n = self.nElementos()
        if indice == n:
            lista.insertarNodoFinal(val)
        elif indice == n-1:
            nuevoNodo = NodoLista(val)
            panterior = self.pfinal
            self.pfinal = nuevoNodo
            self.pfinal.puntero = panterior
            self.pfinal = self.pfinal.puntero
        elif indice == 0:
            nuevoNodo = NodoLista(val)
            nuevoNodo.puntero = self.pinicio
            self.pinicio = nuevoNodo
        else:
            panterior = self.pinicio
            i = 0
            while indice-i != 1:
                panterior = panterior.puntero
                i += 1
            psiguiente = panterior.puntero
            nuevoNodo = NodoLista(val)
            panterior.puntero = nuevoNodo
            panterior = panterior.puntero
            panterior.puntero = psiguiente

    def recorrerLista(self):
        paux = self.pinicio
        while paux != None:
            print(paux.valor)
            paux = paux.puntero

print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v!="S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoFinal(v)

n = lista.nElementos()

i = int(input("Ingrese el indice en en el cual quiera insertar el nuevo elemento: "))

while i<0 or i>n:
    print("Error, indice imposible")
    i = int(input("Ingrese otro indice"))

elemento = input("Ingrese el valor del nuevo elemento: ")

lista.insertarElemento(elemento, i)

print("Nueva Lista:")
lista.recorrerLista()