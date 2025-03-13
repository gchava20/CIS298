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
        # turns the rotor values
        
        }

