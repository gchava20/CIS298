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
        self.ring_setting = 0 

