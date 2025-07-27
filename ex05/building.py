import sys


def building(string: str) -> None:
    '''Print the number of elements in a string
    also the number of each tpye of elements:
    upper-case
    lwer-case
    punctuation
    spaces
    digits'''

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


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        string = input("What is the text to count?\n")
    elif len(args) == 2:
        string = args[1]
    else:
        print("AssertionError: more than one argument is provided")
        exit(1)
    building(string)
