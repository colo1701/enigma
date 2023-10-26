import msvcrt

import enigma_format as enfo
import enigma_rotors as enro

rotors = enro.m3_rotors

letters = ['A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y',
           'Z']

plugs = ['WS', 'RF', 'ZH', 'BU', 'DC', 'GN', 'JM', 'AE']

plugboard = {}

for letter in letters:
    plugboard[letter] = letter
for pair in plugs:
    try:
        plugboard[pair[0]] = pair[1]
        plugboard[pair[1]] = pair[0]
    except:
        pass

def enigma_execute(letter_in: bytes) -> str:
    letter_in = letter_in
    letter_out = plugboard[letter_in]
    return letter_out

if __name__ == '__main__':
    print(enfo.start_string)
    input_list = []
    output_list = []
    while True:
        input = msvcrt.getch().decode("utf-8").upper()
        if input in letters:
            input_list.append(input)
            output_list.append(enigma_execute(input))
            print(f"# INPUT : {''.join(input_list)}\n# OUTPUT: {''.join(output_list)}")
        else:
            print(enfo.stop_string)
            break