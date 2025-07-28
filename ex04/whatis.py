import sys

args = sys.argv

if len(args) < 2:
    exit(0)

if len(args) > 2:
    print("AssertionError: more than one argument is provided")
    exit(1)

number = args[1]

if len(number) == 0:
    exit(0)

if not number.isdigit() and not ((number[0] == '-' or number[0] == '+') and number[1:].isdigit()):
    print("AssertionError: argument is not an integer")
    exit(1)

if len(number) > 1000:
    print("AssertionError: argument is too long")
    exit(1)


if int(number) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
