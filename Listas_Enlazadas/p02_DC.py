class nodolista:
    def __init__(self, valor):
        self.valor= valor
        self.puntero= None
class ListaEnlazada:
    def __init__(self):
        self.pinicial= None
    def insertar_inicio(self, val):
        nuevo= nodolista(val)
        nuevo.puntero= self.pinicial
        self.pinicial= nuevo
    #def mostrar_lista(self):
    #    actual= self.pinicial
    #    while actual!= None:
    #        print(actual.valor, end=", ")
    #        actual= actual.puntero
    #    print("None")
lista= ListaEnlazada()
print("Agregar al comienzo de la lista. Escriba 'fin' para terminar. ")
while True:
    val= input("Ingrese un valor: ")
    if val.lower()== "fin":
        break
    lista.insertar_inicio(val)

#print("Lista enlazada: ")
#lista.mostrar_lista()
    