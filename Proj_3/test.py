import unittest
from enigma import EnigmaMachine

class TestEnigmaMachine(unittest.TestCase):
   class TestEnigmaMachine(unittest.TestCase):
    def setUp(self):
        self.rotor_config = [(1, 0), (2, 0), (3, 0)]
        self.plug_settings = "AB CD EF"
        self.reflector_type = 'B'
        self.enigma = EnigmaMachine(self.rotor_config, self.plug_settings, self.reflector_type)

    def test_encoding(self):
        encoded = self.enigma.encode_message("HELLO")
        self.assertEqual(encoded, "FBONZ")

    def test_decoding(self):
        encoded = self.enigma.encode_message("HELLO")
        self.enigma = EnigmaMachine(self.rotor_config, self.plug_settings, self.reflector_type)
        decoded = self.enigma.encode_message(encoded)
        self.assertEqual(decoded, "HELLO")

    def test_consistency(self):
        encoded1 = self.enigma.encode_message("HELLO")
        encoded2 = self.enigma.encode_message("HELLO")
        self.assertEqual(encoded1, encoded2)

    def test_non_alphabetic_input(self):
        encoded = self.enigma.encode_message("HELLO123")
        self.assertEqual(encoded, "FBONZ")

if __name__ == '__main__':
    unittest.main()