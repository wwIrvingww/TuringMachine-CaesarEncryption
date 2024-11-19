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

    def initialize_tapes(self, input1, input2, input3):
        # Inicializar cinta 1 con la entrada y cintas 2 y 3 vacías
        self.tape1 = list(input1) + ['_']
        self.tape2 = list(input2)+['_']
        self.tape3 = list(input3)+['_']

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
        
        ## parse key
        possible_keys = []
        var_storage = ""
        all_trans = list(self.transitions[self.current_state].keys())
        for trans in all_trans:
            positions = trans.split(",")
            if((symbol1 == positions[0] or positions[0] in ["#","var"]) 
               and (symbol2 == positions[1] or positions[1] in ["#","var"]) 
               and (symbol3== positions[2]or positions[2] in ["#","var"])):

                possible_keys.append(trans)
                if(positions[0]=="var"):
                    var_storage = symbol1
                elif(positions[1]=="var"):
                    var_storage = symbol2
                elif(positions[2]=="var"):
                    var_storage = symbol3

        new_transition_key = min(possible_keys, key=lambda x: x.count('#'))
        
        result = list(self.transitions[self.current_state][new_transition_key])
        for i in range(1,4):
            if(result[i]=="#"):
                result[i]=transition_key.split(",")[i-1]
            elif(result[i]=="var"):
                result[i]=var_storage
        
        new_state, write1, write2, write3, move1, move2, move3 = result
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

    def print_config(self):
        print("State:",self.current_state)
        tape_1 = ""
        for i in range(len(self.tape1)):
            if (i==self.head1):
                tape_1 = tape_1+" *"+self.tape1[i]
            else:
                tape_1 = tape_1+self.tape1[i]
        print("Tape 1:",tape_1)
        
        tape_2 = ""
        for i in range(len(self.tape2)):
            if (i==self.head2):
                tape_2 = tape_2+" *"+self.tape2[i]
            else:
                tape_2 = tape_2+self.tape2[i]
        print("Tape 2:",tape_2)
        
        tape_3 = ""
        for i in range(len(self.tape3)):
            if (i==self.head3):
                tape_3 = tape_3+" *"+self.tape3[i]
            else:
                tape_3 = tape_3+self.tape3[i]
        print("Tape 3:",tape_3)

    def run(self):
        while self.current_state not in [self.accept_state, self.reject_state]:
            self.print_config()
            status = self.step()
            print("")

        print(f"Final State: {self.current_state}, Tape1: {''.join(self.tape1)}, Tape2: {''.join(self.tape2)}, Tape3: {''.join(self.tape3)}")
        return self.current_state == self.accept_state
    
