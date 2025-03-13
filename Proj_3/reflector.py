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
