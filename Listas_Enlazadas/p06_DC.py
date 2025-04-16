class nodolista:
    def __init__(self, valor):
        self.valor= valor
        self.puntero= None
class ListaEnlazada:
    def __init__(self):
        self.pinicial= None
    def insertar_final(self, valor):
        nuevo= nodolista(valor)
        if self.pinicial== None:
            self.pinicial= nuevo
        else:
            actual= self.pinicial
            while actual.puntero!= None:
                actual= actual.puntero
            actual.puntero= nuevo
    def mostrar_lista(self):
        actual= self.pinicial
        while actual!= None:
            print(actual.valor, end=", ")
            actual = actual.puntero
        print("None")
    def eliminar_nodo(self, valor):
        actual= self.pinicial
        anterior= None
        if actual!= None and actual.valor== valor:
            self.pinicial= actual.puntero
            actual= None
            return
        while actual!= None and actual.valor!= valor:
            anterior= actual
            actual= actual.puntero
        if actual== None:
            print("El valor", valor," no esta en la lista.")
            return
        anterior.puntero= actual.puntero
        actual= None

lista= ListaEnlazada()
print("Agregue elementos a la lista enlazada. Escriba 'fin' para terminar.")
while True:
    val= input("Ingrese un valor: ")
    if val.lower()== "fin":
        break
    lista.insertar_final(val)
print("Lista enlazada: ")
lista.mostrar_lista()
valor_eliminar= input("Ingrese el valor a eliminar de la lista: ")
lista.eliminar_nodo(valor_eliminar)
print("La lista final: ")
lista.mostrar_lista()