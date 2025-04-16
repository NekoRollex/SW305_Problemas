class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Algo salio mal")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def parentesis(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter == "(":
            pila.push(caracter)
        elif caracter == ")":
            if pila.is_empty():
                return False
            pila.pop()
    
    return pila.is_empty()

expresion = input("Ingrese la expresion: ")

if parentesis(expresion):
    print("Los parentesis estan balanceados")
else:
    print("Los parentesis no estan balanceados")