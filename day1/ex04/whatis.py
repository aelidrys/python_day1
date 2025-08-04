import sys


args = sys.argv

if len(args) < 2:
    exit(0)

try:
    assert len(args) <= 2, "more than one argument is provided"
except AssertionError as e:
    print(f"AssertionError: {e}")
    exit(1)

number = args[1]

try:
    try:
        int(number)
    except ValueError as e:
        raise AssertionError("argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
    exit(1)

if len(number) == 0:
    exit(0)

try:
    assert len(number) < 1000, "argument is too long"
except AssertionError as e:
    print(f"AssertionError: {e}")
    exit(1)

if int(number) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
