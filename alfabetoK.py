def process_input(input_string):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # Separar el desplazamiento (k) y el texto
    parts = input_string.split("#")
    if len(parts) != 3:
        raise ValueError("El formato del input debe ser 'k # texto'")
    try:
        k = int(parts[0].strip())  # Extraer y convertir k a entero
    except:
        try:
            k = alphabet.index(parts[0].strip().upper())
        except:
            raise ValueError("k debe ser un numero o una letra del alfabeto")
    text = parts[1].strip()   # Obtener el texto después de '#'

    if(parts[2].strip().lower()!="encriptar"):
        k = 26-k
    # Generar alfabeto español
    
    # Desplazar el alfabeto
    k = k % len(alphabet)  # Asegurar que k esté dentro del rango del alfabeto
    shifted_alphabet = alphabet[k:] + alphabet[:k]

    return text,alphabet, shifted_alphabet

