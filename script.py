import sys

def palabras_intersectadas(text1, text2):
    # Obtener las palabras de cada cadena
    palabras1 = set(text1.split())
    palabras2 = set(text2.split())

    # Encontrar las palabras intersectadas
    intersectadas = palabras1.intersection(palabras2)

    return intersectadas

# Check if the required number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py text1 text2")
else:
    text1 = sys.argv[1]
    text2 = sys.argv[2]
    resultado = palabras_intersectadas(text1, text2)
    print(resultado)
