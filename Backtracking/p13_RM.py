n = int(input("Ingresar el tamaño del set: "))
print("Ingrese los valores del set")

lista = []
for i in range(n):
    lista.append(int(input()))

x = int(input("Valor objetivo: "))

def find_subset(i, suma, indices):
    if i == n:
        if suma == x:
            ans = set()
            for i in indices:
                ans.add(lista[i])
            print("subset:", ans)
            return True
        return False
    if suma > x:
        return False
    if find_subset(i+1, suma, indices):
        return True
    indices.append(i)
    if find_subset(i+1, suma + lista[i], indices):
        indices.pop()
        return True
    indices.pop()
    return False

if not find_subset(0, 0, []):
    print("No hay subset")
    