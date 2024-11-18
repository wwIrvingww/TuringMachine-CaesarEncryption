import json

class TuringMachineThreeTape:
    def __init__(self, config):
        # Cargar configuración
        self.states = config["states"]
        self.input_symbols = config["input_symbols"]
        self.tape_symbols = config["tape_symbols"]
        self.initial_state = config["initial_state"]
        self.accept_state = config["accept_state"]
        self.reject_state = config["reject_state"]
        self.transitions = config["transitions"]
        self.current_state = self.initial_state

        # Inicializar cintas y cabezales
        self.tape1 = ['_']
        self.tape2 = ['_']
        self.tape3 = ['_']
        self.head1 = 0
        self.head2 = 0
        self.head3 = 0

    def initialize_tapes(self, input_string):
        # Inicializar cinta 1 con la entrada y cintas 2 y 3 vacías
        self.tape1 = list(input_string) + ['_']
        self.tape2 = ['_']
        self.tape3 = ['_']

    def step(self):
        if self.current_state == self.accept_state:
            return "Accepted"
        if self.current_state == self.reject_state:
            return "Rejected"

        # Leer símbolos de las tres cintas
        symbol1 = self.tape1[self.head1]
        symbol2 = self.tape2[self.head2]
        symbol3 = self.tape3[self.head3]
        transition_key = f"{symbol1},{symbol2},{symbol3}"

        # Verificar transición específica
        if transition_key in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][transition_key]
        # Verificar transición con comodines en varias combinaciones
        elif f"#,{symbol2},{symbol3}" in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][f"#,{symbol2},{symbol3}"]
            write1 = symbol1  # Mantener el símbolo actual de la cinta 1
        elif f"{symbol1},#,{symbol3}" in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][f"{symbol1},#,{symbol3}"]
            write2 = symbol2  # Mantener el símbolo actual de la cinta 2
        elif f"{symbol1},{symbol2},#" in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][f"{symbol1},{symbol2},#"]
            write3 = symbol3  # Mantener el símbolo actual de la cinta 3
        elif f"#,#,{symbol3}" in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][f"#,#,{symbol3}"]
            write1, write2 = symbol1, symbol2  # Mantener los símbolos actuales en cintas 1 y 2
        elif f"#,{symbol2},#" in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][f"#,{symbol2},#"]
            write1, write3 = symbol1, symbol3  # Mantener los símbolos actuales en cintas 1 y 3
        elif f"{symbol1},#,#" in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][f"{symbol1},#,#"]
            write2, write3 = symbol2, symbol3  # Mantener los símbolos actuales en cintas 2 y 3
        elif f"#,#,#" in self.transitions.get(self.current_state, {}):
            new_state, write1, write2, write3, move1, move2, move3 = self.transitions[self.current_state][f"#,#,#"]
            write1, write2, write3 = symbol1, symbol2, symbol3  # Mantener los símbolos actuales en todas las cintas
        else:
            # Si no hay transición válida, ir al estado de rechazo
            self.current_state = self.reject_state
            return "Rejected"


        # Actualizar estado y cintas
        self.current_state = new_state
        self.tape1[self.head1] = write1
        self.tape2[self.head2] = write2
        self.tape3[self.head3] = write3

        # Mover cabezales
        self.move_head(move1, 1)
        self.move_head(move2, 2)
        self.move_head(move3, 3)

        return "Running"

    def move_head(self, direction, tape_number):
        if tape_number == 1:
            if direction == 'R':
                self.head1 += 1
                if self.head1 >= len(self.tape1):
                    self.tape1.append('_')
            elif direction == 'L':
                self.head1 -= 1
                if self.head1 < 0:
                    self.tape1.insert(0, '_')
                    self.head1 = 0
        elif tape_number == 2:
            if direction == 'R':
                self.head2 += 1
                if self.head2 >= len(self.tape2):
                    self.tape2.append('_')
            elif direction == 'L':
                self.head2 -= 1
                if self.head2 < 0:
                    self.tape2.insert(0, '_')
                    self.head2 = 0
        elif tape_number == 3:
            if direction == 'R':
                self.head3 += 1
                if self.head3 >= len(self.tape3):
                    self.tape3.append('_')
            elif direction == 'L':
                self.head3 -= 1
                if self.head3 < 0:
                    self.tape3.insert(0, '_')
                    self.head3 = 0

    def run(self):
        while self.current_state not in [self.accept_state, self.reject_state]:
            print(f"State: {self.current_state}, Tape1: {''.join(self.tape1)}, Head1: {self.head1}, Tape2: {''.join(self.tape2)}, Head2: {self.head2}, Tape3: {''.join(self.tape3)}, Head3: {self.head3}")
            status = self.step()

        print(f"Final State: {self.current_state}, Tape1: {''.join(self.tape1)}, Tape2: {''.join(self.tape2)}, Tape3: {''.join(self.tape3)}")
        return self.current_state == self.accept_state

