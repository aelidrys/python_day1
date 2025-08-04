import sys
from ft_filter import ft_filter


def filterstring(string: str, lessLen: int):
    '''filterstring(string: str, lessLen :int) --> list

Return a list of strings that have a length greater than the lessLen
and do not contain punctuation characters or invisible characters.'''

    def isVlaid(str, lessLen):
        punctuationChas = "\"!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"
        if len(str) <= lessLen:
            return False
        if [c for c in str if c in punctuationChas]:
            return False
        if not str.isprintable():
            return False
        return True

    strs = string.split()
    filtredStrs = ft_filter(lambda s: isVlaid(s, lessLen), strs)
    return filtredStrs


def main():
    '''main() --> None
Check is the arguments are valid and call filterstring function.'''
    args = sys.argv

    try:
        assert len(args) == 3, "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(0)

    lessLen = 0
    try:
        try:
            lessLen = int(args[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(0)

    string = args[1]
    filtredStrs = filterstring(string, lessLen)
    print(list(filtredStrs))


if __name__ == "__main__":
    main()
