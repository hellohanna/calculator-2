"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from functools import reduce




while True:
    breakout = False

    input_string = input('> ')
    input_string = input_string.rstrip()
    tokens = input_string.split(" ")
    cmd = tokens[0]

    if cmd == "q":
        break

    numbers = []
    for token in tokens[1:]:
        try:
            num = float(token)
        except  ValueError:
            print("Please enter valid numbers. Try again...") 
            breakout = True
            continue

    if breakout == True:
        continue

    numbers.append(float(token))


    if cmd == '+':
        result = reduce(add, numbers)
    elif cmd == "-":
        result = reduce(subtract, numbers)
    elif cmd == "*":
        result = reduce(multiply, numbers)
    elif cmd == "/":
        result = reduce(divide, numbers)
    elif cmd == "pow":
        result = power(numbers)
    elif cmd == "mod":
        result = reduce(mod, numbers)
    elif cmd == 'cube':
        if len(numbers) > 1:
            print ("Too many numbers")
            continue
        result = power([numbers[0], 3])
    elif cmd == 'square':
        if len(numbers) > 1:
            print ("Too many numbers")
            continue
        result = power([numbers[0], 2])
    else:         
        print("Invalid calculation operation. Try again.")


    print(result)

