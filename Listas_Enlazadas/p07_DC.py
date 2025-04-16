class NodoLista:
    def __init__(self, valor):
        self.valor = valor
        self.puntero = None
class ListaEnlazada:
    def __init__(self):
        self.pinicial = None
    def insertar_final(self, valor):
        nuevo = NodoLista(valor)
        if self.pinicial == None:
            self.pinicial = nuevo
        else:
            actual = self.pinicial
            while actual.puntero != None:
                actual = actual.puntero
            actual.puntero = nuevo 
    def insertar_en_posicion(self, valor, posicion):
        nuevo = NodoLista(valor)
        if self.pinicial == None and posicion == 0:
            self.pinicial = nuevo
            return
        actual = self.pinicial
        anterior = None
        cont = 0
        while actual != None and cont < posicion:
            anterior = actual
            actual = actual.puntero
            cont += 1
        if cont == posicion: 
            if anterior != None:
                anterior.puntero = nuevo
                nuevo.puntero = actual
            else:
                self.pinicial = nuevo
                nuevo.puntero = actual
        else:
            print(f"La posición {posicion} está fuera del rango de la lista.")
            return
    def mostrar_lista(self):
        actual = self.pinicial
        while actual != None:
            print(actual.valor, end=", ")
            actual = actual.puntero
        print("None")  
lista = ListaEnlazada()
print("Agregue elementos a la lista enlazada. Escriba 'fin' para terminar.")
while True:
    val = input("Ingrese un valor: ")
    if val.lower() == "fin":
        break
    lista.insertar_final(val) 
print("Lista enlazada: ")
lista.mostrar_lista()
pos = int(input("Ingrese la posición donde desea insertar el valor: ")) - 1
val = input("Ingrese el valor a insertar: ")
lista.insertar_en_posicion(val, pos)
print("Lista final: ")
lista.mostrar_lista()
