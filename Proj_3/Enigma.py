class EnigmaMachine:
    def __init__(self, rotor_num, rotor_pos,plug_settings):
        self.rotors = [] #holds rotor
        self.plugboard = None
        self. reflector = None
    
    def encode_message(self, message):

        pass


class Rotor:
    def __init__(self, rotor_num, start_pos):

        #historical rotor mappings
        self.rotor_mappings = {
            1: "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            2: "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            3: "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            4: "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            5: "VZBRGITYUPSDNHLXAWMJQOFECK"
        }

        self.notch_pos = {
        # turns the rotor values (historical values)
            1: 'Q',  # Q to R
            2: 'E',  # E to F
            3: 'V',  # V to W
            4: 'J',  # J to K
            5: 'Z'   # Z to A
        }

        self.rotor_num = rotor_num
        self.mapping = self.rotor_mappings[rotor_num]
        self.notch = self.notch_pos[rotor_num]
        self.position = start_pos

    def encode(self, char, forward=True):
        offset_value = ord(char) - ord ('A')

        if forward:
            #path moves forward in the rotor
            shift_index_val = (offset_value + self.position) %26
            map_char = self.mapping[shift_index_val]
            output_offset = (ord(map_char) - ord('A') - self.position) % 26
        else:
            shift_index_val = (offset_value + self.position) %26
            index_map = self.mapping.index(chr(shift_index_val + ord('A')))
            output_offset = (index_map - self.position) % 26

        return chr(output_offset + ord('A'))
    
    def rotate(self):
        # rotate rotor by one
        self.position = (self.position + 1) % 26
        return self.position == (ord(self.notch) - ord('A'))
    
class Plugboard:
    def __init__(self, settings):
        self.wiring = {chr(i): chr(i) for i in range(ord('A'), ord('Z')+1)}
        #swap pairs of chars
        for pair in settings.split():
            if len(pair) == 2:
                a, b = pair[0], pair[1]
                self.wiring[a], self.wiring[b] = b, a

    def encode(self, char):
        # swap the chars
        return self.wiring[char]
    
class Reflector:
    def __init__(self, type='B'):
        #reflector wirings
        self.wirings = {
            'A': "EJMZALYXVBWFCRQUONTSPIKHGD", #A wiring
            'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT", #B wiring
            'C': "FVPJIAOYEDRZXWGCTKUQSBNMHL"  #C wiring
        }
        self.mapping = self.wirings[type]

    def reflect(self, char):
        index = ord(char) - ord('A')
        return self.mapping[index]
