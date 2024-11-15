import json

class TuringMachineTwoTape:
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

        # Inicializar las cintas y cabezales
        self.tape1 = ['_']
        self.tape2 = ['_']
        self.head1 = 0
        self.head2 = 0

    def initialize_tapes(self, input_string):
        # Inicializar cinta 1 con la entrada y cinta 2 vacía
        self.tape1 = list(input_string) + ['_']
        self.tape2 = ['_']

    def step(self):
        if self.current_state == self.accept_state:
            return "Accepted"
        if self.current_state == self.reject_state:
            return "Rejected"

        # Leer símbolos de ambas cintas
        symbol1 = self.tape1[self.head1]
        symbol2 = self.tape2[self.head2]
        transition_key = f"{symbol1},{symbol2}"

        # Verificar transición
        if transition_key not in self.transitions.get(self.current_state, {}):
            self.current_state = self.reject_state
            return "Rejected"

        # Obtener nueva configuración
        new_state, write1, write2, move1, move2 = self.transitions[self.current_state][transition_key]

        # Escribir en las cintas
        self.tape1[self.head1] = write1
        self.tape2[self.head2] = write2
        self.current_state = new_state

        # Mover cabezales
        self.move_head(move1, 1)
        self.move_head(move2, 2)

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

    def run(self):
        while self.current_state not in [self.accept_state, self.reject_state]:
            print(f"State: {self.current_state}, Tape1: {''.join(self.tape1)}, Head1: {self.head1}, Tape2: {''.join(self.tape2)}, Head2: {self.head2}")
            status = self.step()

        print(f"Final State: {self.current_state}, Tape1: {''.join(self.tape1)}, Tape2: {''.join(self.tape2)}")
        return self.current_state == self.accept_state
