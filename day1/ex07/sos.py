import sys


def sos(arg: str) -> str:

    '''sos(arg: str) --> str

Convert a string to Morse code.'''

    msg = "the arguments are bad"
    try:
        assert all(c.isalnum() or c.isspace() for c in arg), msg
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)

    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/',
    }
    morse_str = ' '.join(morse_code[c] for c in arg.upper() if c in morse_code)
    return morse_str


def main():
    '''main() --> None
Accept only one argument and convert it to Morse code.'''
    args = sys.argv

    try:
        assert len(args) == 2, "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(0)

    arg = args[1]
    morse_code = sos(arg)
    print(morse_code)


if __name__ == "__main__":
    main()
