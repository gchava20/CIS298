import unittest
from enigma import EnigmaMachine

def run_enigma_simulation():
    try:
        rotor_input = input("Enter rotor numbers and start positions(e.g., '1 0 2 0 3 0' for Rotor 1 at 0, Rotor 2 at 0, Rotor 3 at 0): ")
        rotor_parts = rotor_input.split()
        if len(rotor_parts) != 6:
            raise ValueError("Enter three rotor numbers and three start positions.")
        rotor_configurations = [(int(rotor_parts[i]), int(rotor_parts[i+1])) for i in range(0, 6, 2)]
        
        plugboard_settings = input("Enter plugboard settings (e.g., 'AB CD EF'): ")
        
        reflector_type = input("Enter reflector type (B or C, default is B if not specified): ")
        reflector_type = reflector_type.upper() if reflector_type in ['B', 'C'] else 'B'
        
        enigma_machine = EnigmaMachine(rotor_configurations, plugboard_settings, reflector_type)
        
        message = input("Enter the message to encode/decode: ")
        processed_message = enigma_machine.encode_message(message)
        
        print("Processed message:", processed_message)
    except Exception as e:
        print("Error:", str(e))

def run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromName('test')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    with open('test_results.txt', 'w') as f:
        f.write(f"Ran {result.testsRun} tests.\n")
        if not result.wasSuccessful():
            f.write("Some tests failed:\n")
            for failed in result.failures:
                f.write(f"{failed[0]}: {failed[1]}\n")
        else:
            f.write("All tests passed successfully.\n")


if __name__ == '__main__':
    choice = input("Type 'run' to start the Enigma or 'test' to run unit tests: ").lower()
    if choice == 'test':
        run_tests()
    elif choice == 'run':
        run_enigma_simulation()