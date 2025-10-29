import sys

valueError = False #user-defined variable, not calling the error

print("Welcome to the Calculator")

try:
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
except ValueError:
    valueError = True
    print("error: invalid characters")
    
    while valueError == True:
        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))
            valueError = False
        except ValueError:
            valueError = True
            print("error: invalid characters")

operation = input("enter your operation (+ (addition), - (subtraction), * (multiplication), / (division)): ")

if operation == "+":
    answer = num1 + num2
    print("Your answer is " + str(answer))
elif operation == "-":
    answer = num1 - num2
    print("Your answer is " + str(answer))
elif operation == "*":
    answer = num1 * num2
    print("Your answer is " + str(answer))
elif operation == "/":
    answer = num1 / num2
    print("Your answer is " + str(answer))
else:
    print("error: invalid operation entered")