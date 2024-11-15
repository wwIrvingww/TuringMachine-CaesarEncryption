import json
from turing_machine import TuringMachineTwoTape

# Cargar configuración desde el archivo JSON
with open("machine_config.json", "r") as file:
    config = json.load(file)

# Inicializar la máquina de Turing
tm = TuringMachineTwoTape(config)

# Leer la entrada del archivo de prueba
with open("test.txt", "r") as file:
    input_string = file.read().strip()

# Inicializar las cintas con la entrada
tm.initialize_tapes(input_string)

# Ejecutar la máquina de Turing
result = tm.run()
if result:
    print("La máquina de Turing aceptó la cadena.")
else:
    print("La máquina de Turing rechazó la cadena.")
