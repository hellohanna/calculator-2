"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    input_string = input('> ')
    input_string = input_string.rstrip()
    tokens = input_string.split(" ")
    cmd = tokens[0]

    if cmd == "q":
        break;

    if (len(tokens) < 2 or len(tokens) > 3):
        print ("Invalid number of numbers. Try again.")
        continue

        
    num1 = float(tokens[1])

    #### we might not have two numbers.
    if len(tokens) > 2:
        num2 = float(tokens[2])

    if( len(tokens) == 3):
        if cmd == '+':
            result = add(num1, num2)
        elif cmd == "-":
            result = subtract(num1, num2)
        elif cmd == "*":
            result = multiply(num1, num2)
        elif cmd == "/":
            result = divide(num1, num2)
        elif cmd == "pow":
            result = power(num1, num2)
        elif cmd == "mod":
            result = mod(num1, num2)
        else:         
            print("Invalid calculation operation. Try again.")
    elif (len(tokens)==2):
        if cmd == "square":
            result = square(num1)
        elif cmd == "cube":
            result = cube(num1)
        else:         
            print("Invalid calculation operation. Try again.")
    else:
        print ("Invalid number of numbers. Try again.")
        continue

    print(result)

