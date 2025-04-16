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
    def ordenar_lista(self):
        if self.pinicial== None or self.pinicial.puntero== None:
            return
        flag= True
        while flag:
            flag= False
            actual= self.pinicial
            while actual.puntero!= None:
                if actual.valor>actual.puntero.valor:
                    temp= actual.valor
                    actual.valor= actual.puntero.valor
                    actual.puntero.valor= temp
                    flag= True
                actual= actual.puntero
    def mostrar_lista(self):
        actual= self.pinicial
        while actual!= None:
            print(actual.valor, end=", ")
            actual = actual.puntero
        print("None")

lista= ListaEnlazada()
print("Agregue elementos a la lista enlazada. Escriba 'fin' para terminar.")
while True:
    val= input("Ingrese un valor: ")
    if val.lower()== "fin":
        break
    lista.insertar_final(val)
print("Lista enlazada: ")
lista.mostrar_lista()
lista.ordenar_lista()
print("Lista ordenada: ")
lista.mostrar_lista()