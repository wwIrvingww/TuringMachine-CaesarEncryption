import json
from turing_machine import TuringMachineThreeTape
from alfabetoK import  process_input
from construct_machine import construct_machine

# Leer la entrada del archivo de prueba
with open("test.txt", "r") as file:
    input_string = file.read().strip()

# Convertir entrada a cintas
tem_text, alphabet, k_alphabet = process_input(input_string)
text = tem_text.upper()
print(text)
print(alphabet)
print(k_alphabet)


construct_machine(alphabet)
# Cargar configuración desde el archivo JSON
with open("machine_config.json", "r") as file:
    config = json.load(file)

# Inicializar la máquina de Turing
tm = TuringMachineThreeTape(config)

# Inicializar las cintas con la entrada
tm.initialize_tapes(text, alphabet, k_alphabet)

# Ejecutar la máquina de Turing
result = tm.run()
if result:
    print("La máquina de Turing aceptó la cadena.")
else:
    print("La máquina de Turing rechazó la cadena.")
