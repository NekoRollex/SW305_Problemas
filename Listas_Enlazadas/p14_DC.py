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
    def invertir_lista(self):
        anterior= None
        actual= self.pinicial
        while actual!= None:
            siguiente= actual.puntero
            actual.puntero= anterior
            anterior= actual
            actual= siguiente
        self.pinicial= anterior
    def es_palindromo(self):
        original= self.pinicial
        self.invertir_lista()
        actual_original= original
        actual_invertida= self.pinicial
        while actual_original!= None:
            if actual_original.valor!= actual_invertida.valor:
                return False
            actual_original= actual_original.puntero
            actual_invertida= actual_invertida.puntero
        return True
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
if lista.es_palindromo():
    print("La lista es un palíndromo.")
else:
    print("La lista no es un palíndromo.")