import sys


def building(string: str) -> None:
    '''building(string: str) --> None
Print the number of all characters in a string
also the number of its upper-case characters, lower-case characters,
    punctuation characters, digits and spaces.'''

    digits = 0
    punctuation = 0
    upperCase = 0
    lowerCase = 0
    spaces = 0
    punctuationChars = "\"!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"

    for char in string:
        if char.isdigit():
            digits += 1
        elif char in punctuationChars:
            punctuation += 1
        elif char.isupper():
            upperCase += 1
        elif char.islower():
            lowerCase += 1
        elif char.isspace():
            spaces += 1

    print(f"The text contains {len(string)} Characters:")
    print(f"{upperCase} upper letters")
    print(f"{lowerCase} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    '''main() --> None
Get the string from command line args or input and call building function.'''

    args = sys.argv

    try:
        assert len(args) <= 2, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(0)

    if len(args) == 1:
        print("What is the text to count?")
        string = sys.stdin.read()
    elif len(args) == 2:
        string = args[1]

    building(string)


if __name__ == "__main__":
    main()
