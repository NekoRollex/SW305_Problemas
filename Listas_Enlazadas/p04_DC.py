class nodolista:
    def __init__(self, valor):
        self.valor= valor
        self.puntero= None
class ListaEnlazada:
    def __init__(self):
        self.pinicial= None
    def insertar_final(self, valor):
        nuevo= nodolista(valor)
        if self.pinicial==None:
            self.pinicial= nuevo
        else:
            actual= self.pinicial
            while actual.puntero!= None:
                actual= actual.puntero
            actual.puntero= nuevo
    def contador_lista(self):
        cont= 0
        actual= self.pinicial
        while actual!= None:
            cont +=1
            actual= actual.puntero
        return cont
lista= ListaEnlazada()
print("Agregue elementos a la lista enlazada. Escriba 'fin' para terminar.")
while True:
    val= input("Ingrese un valor: ")
    if val.lower()== "fin":
        break
    lista.insertar_final(val)
num= lista.contador_lista()
print("El numero de nodos en la lista es: ", num)