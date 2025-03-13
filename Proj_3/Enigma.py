from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor

class EnigmaMachine:
    def __init__(self, rotor_config, plug_settings, reflector_type='B'):
        self.rotors = [Rotor(rotor_num, start_pos) for rotor_num, start_pos in rotor_config]
        self.plugboard = Plugboard(plug_settings)
        self.reflector = Reflector(reflector_type)
    
    def encode_message(self, message):
        message_en = ""
        for char in message.upper():
            if char.isalpha(): 
                step_char = self.plugboard.encode(char)
                
                for rotor in self.rotors:
                    step_char = rotor.encode(step_char)
        
                step_char = self.reflector.reflect(step_char)
                
                for rotor in reversed(self.rotors):
                    step_char = rotor.encode(step_char, forward=False)
                
                step_char = self.plugboard.encode(step_char)
                
                message_en += step_char
                
                for i in range(len(self.rotors)):
                    if not self.rotors[i].rotate():
                        break
        return message_en