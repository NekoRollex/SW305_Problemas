class NodoLista:
    def __init__(self, valor):
        self.valor = valor
        self.punt = None

class ListaEnlazada:
    def __init__(self):
        self.pinicio = None
        self.pfinal = None

    def insertarNodoFinal(self, valor):
        nuevoNodo = NodoLista(valor)
        if self.pinicio is None:
            self.pinicio = nuevoNodo
            self.pfinal = nuevoNodo
        else:
            self.pfinal.punt = nuevoNodo
            self.pfinal = nuevoNodo

    def insertarNodoInicio(self, valor):
        nuevoNodo = NodoLista(valor)
        if self.pinicio is None:
            self.pinicio = nuevoNodo
            self.pfinal = nuevoNodo
        else:
            nuevoNodo.punt = self.pinicio
            self.pinicio = nuevoNodo

    def recorrerLista(self):
        actual = self.pinicio
        while actual:
            print(actual.valor, end=" ")
            actual = actual.punt
    
lista = ListaEnlazada() 

print("Agregar elementos ('S' para terminar)")

while True:
    elemento = input("Ingresa el elemento: ")
    if elemento.upper() == 'S':
        break
    if not elemento:
        print("Elemento no puede ser vacio. Ingrese un elemento que sea valido")
        continue
    while True:
        insertar = input("¿Insertar nodo al inicio (ingrese 'I') o al final (ingrese 'F')?: ").upper()
        if insertar == 'I' or insertar == 'F':
            break
        else:
            print("Opcion invalida. Ingrese 'I' o 'F'")

    if insertar == 'I':
        lista.insertarNodoInicio(elemento)
    elif insertar == 'F':
        lista.insertarNodoFinal(elemento)

print("Lista:")
lista.recorrerLista()