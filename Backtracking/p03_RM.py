print("Se va a permutar los valores del 1 al n")
n = int(input("n: "))

def permutar(n, lista=[]):
    if len(lista) == n:
        print(lista)
    else:
        for i in range(1, n+1):
            if i not in lista:
                lista.append(i)
                permutar(n, lista)
                lista.pop()

print("\nLas permutaciones son:")
permutar(n)