# More advanced python calculator
# User inputs first number, chooses function (+ - * /)
# Then enters second number for result

# Variables

num1 = float(input("> "))
op = raw_input("> ")
num2 = float(input("> "))

# "if" used to check a condition
# Example: check that the coniditon is a + (addition) or - (subtraction)

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)

else:
    print("Invalid Input")