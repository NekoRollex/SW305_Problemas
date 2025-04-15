class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
class Pila:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nodo = Nodo(valor)
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
            
    def is_empty(self):
        return self.cima is None
    

def resultadoPostfija(listaPost):
    pila = Pila()

    for valor in listaPost:
        if valor == '+':
            a = pila.peek()
            pila.pop()
            b = pila.peek()
            pila.pop()
            if a is None or b is None:
                return "Error (Expresión inválida)."
            pila.push(a+b)
        elif valor == '-':
            a = pila.peek()
            pila.pop()
            b = pila.peek()
            pila.pop()
            if a is None or b is None:
                return "Error (Expresión inválida)."
            pila.push(b-a)
        elif valor == '*':
            a = pila.peek()
            pila.pop()
            b = pila.peek()
            pila.pop()
            if a is None or b is None:
                return "Error (Expresión inválida)."
            pila.push(a*b)
        elif valor == '/':
            a = pila.peek()
            pila.pop()
            b = pila.peek()
            pila.pop()
            if a is None or b is None:
                return "Error (Expresión inválida)."
            pila.push(b/a)
        else:
            pila.push(int(valor))

    resultado = pila.peek()
    pila.pop()

    if resultado is None or not pila.is_empty():
        return "Error (Expresión inválida)."
    return resultado

post = input("Ingrese la expresión postfija: ")
listaPost = post.split()

print("Resultado de la expresión postfija:", resultadoPostfija(listaPost))
