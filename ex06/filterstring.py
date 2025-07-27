import sys

def filterstring(string: str, lessLen):
    list_strs = string.split(" ")
    filtredStrs = [word for word in list_strs if len(word) >= lessLen]
    return filtredStrs

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print(f"AssertionError: invalid number of argument.")
        exit(1)
    string = str(args[1])
    if string is None:
        print(f"AssertionError: invalid argument.")
        exit(1)
    number = args[2]
    if number.isdigit() is False and not(number[0] == '+' and number[1:].isdigit() is True):
        print(f"AssertionError: invalid argument.")
        exit(1)
    lessLen = int(number)
    filtredStrs = filterstring(string, lessLen)
    print(filtredStrs)

