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
    def fusionar_listas(self, lista2):
        lista_fusionada= ListaEnlazada()
        actual1= self.pinicial
        actual2= lista2.pinicial
        while actual1!= None and actual2!= None:
            if actual1.valor<actual2.valor:
                lista_fusionada.insertar_final(actual1.valor)
                actual1= actual1.puntero
            else:
                lista_fusionada.insertar_final(actual2.valor)
                actual2= actual2.puntero
        while actual1!= None:
            lista_fusionada.insertar_final(actual1.valor)
            actual1= actual1.puntero
        while actual2!= None:
            lista_fusionada.insertar_final(actual2.valor)
            actual2= actual2.puntero
        return lista_fusionada
    def mostrar_lista(self):
        actual= self.pinicial
        while actual!= None:
            print(actual.valor, end=", ")
            actual = actual.puntero
        print("None")

lista1= ListaEnlazada()
lista2= ListaEnlazada()

print("Agregue elementos a la 1ra lista enlazada. Escriba 'fin' para terminar.")
while True:
    val= input("Ingrese un valor: ")
    if val.lower()== "fin":
        break
    lista1.insertar_final(val)
lista1.ordenar_lista()
print("Lista 1 ordenada: ")
lista1.mostrar_lista()
print("Agregue elementos a la 2da lista enlazada. Escriba 'fin' para terminar.")
while True:
    val= input("Ingrese un valor: ")
    if val.lower()== "fin":
        break
    lista2.insertar_final(val)
lista2.ordenar_lista()
print("Lista 2 ordenada: ")
lista2.mostrar_lista()
fusion= lista1.fusionar_listas(lista2)
print("Lista fusionada: ")
fusion.mostrar_lista()