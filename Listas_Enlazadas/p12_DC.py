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
    def encontrar_nodo_medio(self):
        total_nodos= 0
        actual= self.pinicial
        while actual!= None:
            total_nodos+= 1
            actual= actual.puntero
        if total_nodos == 0:
            return None
        medio_pos= total_nodos//2
        actual= self.pinicial
        for _ in range(medio_pos):
            actual= actual.puntero
        
        if total_nodos%2!=0:
            return actual.valor
        else:
            return (actual.valor+actual.puntero.valor)/2
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
    lista.insertar_final(int(val))
print("Lista enlazada: ")
lista.mostrar_lista()
medio= lista.encontrar_nodo_medio()
if medio!= None:
    print("El nodo medio es:", medio)
else:
    print("La lista esta vacia.")