class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pila:
    def __init__(self):
        self.top = None

    def push(self, valor):
        nodo = NodoPila(valor)
        nodo.next = self.top
        self.top = nodo
    
    def pop(self):
        if not self.is_empty():
            nodo = self.top
            self.top = nodo.next
            return nodo.valor
        return None

    def is_empty(self):
        return self.top is None

def validar_parentesis(expresion):
    if expresion[0] == ')':
        return False
    pila = Pila()
    
    for caracter in expresion:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.is_empty():
                return False
            pila.pop()
    
    return pila.is_empty()

expresion = input("Ingrese una expresión con paréntesis: ")

if validar_parentesis(expresion):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")
