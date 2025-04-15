class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.minimo = valor
        self.siguiente = None
        
class Pila:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nodo = Nodo(valor)
        if self.cima is not None:
            nodo.minimo = min(valor, self.cima.minimo)
        nodo.siguiente = self.cima
        self.cima = nodo
    
    def pop(self):
        nodo = self.cima
        if not self.is_empty():
            self.cima = nodo.siguiente

    def peek(self):
        if not self.is_empty():
            return self.cima.valor
        return None
            
    def minimo(self):
        if not self.is_empty():
            return self.cima.minimo
        return None
    
    def is_empty(self):
        return self.cima is None

pila = Pila()
print("1. push valor")
print("2. pop")
print("3. peek")
print("4. minimo")
print("5. salir")

while True:
    operacion = input("Ingrese la operación: ").split()
    if operacion[0] == "1":
        valor = int(operacion[1])
        pila.push(valor)
    elif operacion[0] == "2":
        pila.pop()
    elif operacion[0] == "3":
        print(pila.peek())
    elif operacion[0] == "4":
        print(pila.minimo())
    elif operacion[0] == "5":
        print("Saliendo...")
        break
    else:
        print("Operación no válida")