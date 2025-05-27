# 30. Transformación de palabras (Word Ladder), transformar una palabra en otra cambiando una letra a la
#     vez, donde cada palabra intermedia debe existir en un diccionario.
#   - Cada palabra es un nodo; BFS encuentra el mínimo número de transformaciones.

from collections import deque

def es_vecina(palabra1, palabra2):
    # Devuelve True si las palabras difieren en solo una letra
    diferencias = sum(a != b for a, b in zip(palabra1, palabra2))
    return diferencias == 1

def BFS_word_ladder(inicial, objetivo, diccionario):
    diccionario = set(diccionario)
    if objetivo not in diccionario:
        return None

    queue = deque([(inicial, [inicial])])
    visitados = set([inicial])

    while queue:
        palabra, camino = queue.popleft()
        if palabra == objetivo:
            return camino

        for i in range(len(palabra)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != palabra[i]:
                    nueva_palabra = palabra[:i] + c + palabra[i+1:]
                    if nueva_palabra in diccionario and nueva_palabra not in visitados:
                        visitados.add(nueva_palabra)
                        queue.append((nueva_palabra, camino + [nueva_palabra]))

    return None

inicial = "hit"
objetivo = "cog"
diccionario = ["hot","dot","dog","lot","log","cog"]

camino = BFS_word_ladder(inicial, objetivo, diccionario)

if camino:
    print(f"Transformación encontrada en {len(camino)-1} pasos:")
    for i, palabra in enumerate(camino):
        print(f"Paso {i}: {palabra}")
else:
    print("No hay transformación posible")