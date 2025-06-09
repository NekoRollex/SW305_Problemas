# 20. Construcción de tabla de carácter malo
#   Patrón: "ABCDABD"
#   -	Construye la tabla de carácter malo para este patrón.
#   -	¿Qué valor tiene cada carácter y por qué?

def construir_tabla_caracter_malo(patron):
    bad_char = {}
    for i, c in enumerate(patron):
        bad_char[c] = i
    return bad_char


patron = "ABCDABD"
tabla = construir_tabla_caracter_malo(patron)

print("Tabla de carácter malo para el patrón:", patron)
for c, pos in tabla.items():
    print(f"Carácter '{c}': última posición = {pos}")