import sys

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

def estaBalanceado(lista):
    pila = Pila()
    for valor in lista:
        if valor == '(':
            pila.push(valor)
        elif valor == ')':
            if pila.is_empty():
                return False
            pila.pop()
    return pila.is_empty()

def convertir_Infija_a_postfija(listaInfija):
    # los parentesis primero
    # prioridad para emparejar son + y -
    # segunda prioridad son * y /
    listaPostfija = []
    # print(listaInfija)

    if len(listaInfija) == 0:
        sys.exit("Error: Expresión inválida.")

    noNumeros = ['+', '-', '*', '/', '(', ')']
    if len(listaInfija) == 1:
        if listaInfija[0] in noNumeros:
            sys.exit("Error: Expresión inválida.")
        return listaInfija

    contador = 0

    pos = -1
    for i in range(len(listaInfija)):
        valor = listaInfija[i]
        if valor == '(':
            contador += 1
        elif valor == ')':
            contador -= 1
        if contador == 0 and (valor == '+' or valor == '-'):
            pos = i
            break

    if pos != -1:
        listaPostfija += convertir_Infija_a_postfija(listaInfija[:pos])
        listaPostfija += convertir_Infija_a_postfija(listaInfija[pos+1:])
        listaPostfija.append(listaInfija[pos])
        return listaPostfija
    
    for i in range(len(listaInfija)):
        valor = listaInfija[i]
        if valor == '(':
            contador += 1
        elif valor == ')':
            contador -= 1
        if contador == 0 and (valor == '*' or valor == '/'):
            pos = i
            break

    if pos != -1:
        listaPostfija += convertir_Infija_a_postfija(listaInfija[:pos])
        listaPostfija += convertir_Infija_a_postfija(listaInfija[pos+1:])
        listaPostfija.append(listaInfija[pos])
        return listaPostfija
    
    if listaInfija[0] == '(' and listaInfija[-1] == ')':
        return convertir_Infija_a_postfija(listaInfija[1:-1])

    sys.exit("Error: Expresión inválida.")

print("Separe los caracteres y números con un espacio.")	
infija = input("Ingrese la expresión infija: ")
listaInfija = infija.split()

if not estaBalanceado(listaInfija):
    print("Error: Paréntesis desbalanceados.")
else:   
    listaPostfija = convertir_Infija_a_postfija(listaInfija)
    print("Expresión postfija:", end=" ")
    for i in listaPostfija:
        print(i, end=" ")    
    print("\nResultado de la expresión postfija:", resultadoPostfija(listaPostfija))
