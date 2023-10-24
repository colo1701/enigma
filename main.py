import msvcrt

letters = ['a', 'b', 'c', 'd', 'e',
           'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y',
           'z']

plugs = ['ws', 'rf', 'zh', 'bu', 'dc', 'gn', 'jm', 'ae']

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
    while True:
        input = msvcrt.getch().decode("utf-8")
        if input in letters:
            print(enigma_execute(input))
        else:
            break