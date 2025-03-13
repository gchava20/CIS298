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