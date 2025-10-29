import sys
print("Welcome to the Calculator")

try:
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
except ValueError:
    print("error: invalid characters")
    sys.exit()

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