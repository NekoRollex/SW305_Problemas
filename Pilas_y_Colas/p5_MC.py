class NodoPila:
    def __init__(self, val):
        self.valor = val
        self.puntero = None

class Pila:
    def __init__(self):
        self.cabeza = None
    
    def push(self, val):
        nodo = NodoPila(val)
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            nodo.puntero = self.cabeza
            self.cabeza = nodo
    
    def pop(self):
        self.cabeza = self.cabeza.puntero
    
    def peek(self):
        paux = self.cabeza
        while paux.puntero != None:
            paux = paux.puntero
        return paux.valor
    
    def isEmpty(self):
        if self.cabeza == None:
            return True
        else:
            return False
    def validarParentesis(self):
        eror = False
        parentesisabiertos = False
        paux = self.cabeza
        while paux != None and eror == False:
            if paux.valor == ")" and parentesisabiertos == False:
                parentesisabiertos = True
            elif paux.valor == "(" and parentesisabiertos == True:
                parentesisabiertos = False
            else:
                eror = True
            paux = paux.puntero
        if parentesisabiertos == True:
            eror = True
        return not eror
    
def leerParentesis(expresionmate):
    pila = Pila()
    i = 0
    while i != len(expresionmate):
        if expresionmate[i] == "(" or expresionmate[i] == ")":
            pila.push(expresionmate[i])
        i += 1
    
    validacion = pila.validarParentesis()
    return validacion



expresionmate = input("Ingrese una expresion matematica: ")
validacion = leerParentesis(expresionmate)

if validacion:
    print("Los parentesis estan validos")
else:
    print("Los parentesis no estan balanceados")