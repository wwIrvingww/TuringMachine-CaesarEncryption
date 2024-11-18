def process_input(input_string):
    # Separar el desplazamiento (k) y el texto
    parts = input_string.split("#")
    if len(parts) != 2:
        raise ValueError("El formato del input debe ser 'k # texto'")
    
    k = int(parts[0].strip())  # Extraer y convertir k a entero
    text = parts[1].strip()   # Obtener el texto después de '#'

    # Generar alfabeto español
    alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    
    # Desplazar el alfabeto
    k = k % len(alphabet)  # Asegurar que k esté dentro del rango del alfabeto
    shifted_alphabet = alphabet[k:] + alphabet[:k]

    return text, shifted_alphabet

# Ejemplo de uso
input_string = "20 # HOLA"
result_text, shifted_alphabet = process_input(input_string)

print(result_text)
print("Alfabeto desplazado:", shifted_alphabet)