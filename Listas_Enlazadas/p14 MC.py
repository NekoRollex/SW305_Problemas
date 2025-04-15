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
    
    def invertirLista(self):
        paux = self.pinicio
        ListaInvertida = ListaEnlazada()
        while paux != None:
            nuevoNodo = NodoLista(paux.valor)
            nuevoNodo.puntero = ListaInvertida.pinicio
            ListaInvertida.pinicio = nuevoNodo
            paux = paux.puntero
        return ListaInvertida
    
    def verificarPalindromo(self):
        palindromo = True
        Listainvertida = ListaEnlazada()
        Listainvertida = self.invertirLista()
        paux = self.pinicio
        paux2 = Listainvertida.pinicio
        while paux != None and paux2 != None and palindromo:
            if paux.valor != paux2.valor:
                palindromo = False
            else:
                paux = paux.puntero
                paux2 = paux2.puntero

        if (paux == None and paux2 != None) or (paux != None and paux2 == None):
            palindromo = False
        return palindromo

print("     Agrega elementos a la lista enlazada   ")
print("Cuando quieras salir ingresa S")

v = None
lista = ListaEnlazada()

while v!="S":
    v = input("Ingrese un elemento: ")
    if v != "S":
        lista.insertarNodoFinal(v)

palindromo = lista.verificarPalindromo()

if palindromo:
    print("La lista es palindorma")
else:
    print("La lista no es palindroma")