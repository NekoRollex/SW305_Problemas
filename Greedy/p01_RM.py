n = int(input("Número de actividades: "))
actividades = []

for i in range(n):
    inicio = int(input(f"Hora de inicio de la actividad {i+1}: "))
    fin = int(input(f"Hora de finalización de la actividad {i+1}: "))
    actividades.append((inicio, fin))

# Ordenar actividades por hora de finalización
for i in range(n):
    for j in range(i+1, n):
        if actividades[i][1] > actividades[j][1]:
            actividades[i], actividades[j] = actividades[j], actividades[i]

indices = []
for i in range(n):
    if i == 0 or actividades[i][0] >= actividades[indices[-1]][1]:
        indices.append(i)

print("\nActividades seleccionadas:")

for i in indices:
    print(f"inicio: {actividades[i][0]}, fin: {actividades[i][1]}")
