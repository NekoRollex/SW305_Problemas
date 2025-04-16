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
    def buscar_valor(self, valor):
        actual= self.pinicial
        while actual!= None:
            if actual.valor== valor:
                return True
            actual= actual.puntero
        return False
lista= ListaEnlazada()
print("Agregue elementos a la lista enlazada. Escriba 'fin' para terminar.")
while True:
    val= input("Ingrese un valor: ")
    if val.lower()== "fin":
        break
    lista.insertar_final(val)
valor= input("Ingrese el valor a buscar: ")
if lista.buscar_valor(valor):
    print("El valor", valor, " existe en la lista")
else:
    print("El valor", valor, "no existe en la lista")