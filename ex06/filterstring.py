import sys


def filterstring(string: str, lessLen: int):
    '''ft_filter(string: str, lessLen :int) --> list

Return an list of strings that have a length greater than the lessLen'''

    def isVlaid(str, lessLen):
        punctuationChas = "\"!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"
        if len(str) <= lessLen:
            return False
        if [c for c in str if c in punctuationChas]:
            return False
        if not str.isprintable():
            return False
        return True

    strs = string.split(" ")
    filtredStrs = [w for w in strs if (lambda w: isVlaid(w, lessLen))(w)]
    return filtredStrs


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print("AssertionError: the arguments are bad")
        exit(1)

    numbr = args[2]
    if not numbr.isdigit() and not (numbr[0] == '+' and numbr[1:].isdigit()):
        print("AssertionError: the arguments are bad")
        exit(1)

    string = args[1]
    lessLen = int(numbr)
    filtredStrs = filterstring(string, lessLen)
    print(filtredStrs)
    print(filterstring.__doc__)
