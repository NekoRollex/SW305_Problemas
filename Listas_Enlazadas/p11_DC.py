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
    def detectar_ciclo(self):
        tortuga= self.pinicial
        liebre= self.pinicial
        while liebre!= None and liebre.puntero!= None:
            tortuga= tortuga.puntero
            liebre= liebre.puntero.puntero
            if tortuga==liebre:
                return True
        return False
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
if lista.detectar_ciclo():
    print("La lista tiene un ciclo")
else:
    print("La lista no tiene un ciclo")