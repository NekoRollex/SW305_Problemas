# Subset Sum Problem (Conjunto de suma objetivo)
# Dado un conjunto de números y un valor objetivo, encontrar si existe un subconjunto cuya suma sea igual a ese valor.
# Poda: Si la suma parcial ya excede el objetivo, se detiene.

def subset_sum(num, objetivo, indice=0, suma_actual=0, sub_actual=[]):
    if suma_actual == objetivo:
        print("Subconjunto encontrado:", sub_actual)
        return True
    if suma_actual > objetivo or indice == len(num):
        return False

    sub_actual.append(num[indice])
    if subset_sum(num, objetivo, indice + 1, suma_actual + num[indice], sub_actual):
        return True
    sub_actual.pop()

    if subset_sum(num, objetivo, indice + 1, suma_actual, sub_actual):
        return True

    return False

conjunto = []
n = int(input("numero de elementos del conjunto: "))
for i in range(n):
    num = int(input(f"Ingrese el elemento {i+1}: "))
    conjunto.append(num)

objetivo = int(input("Ingresa el valor objetivo a calcular: "))

existe = subset_sum(conjunto, objetivo)

if not existe:
    print(f"No existe un subconjunto cuya suma sea {objetivo}")
