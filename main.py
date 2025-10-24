num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

operation = input("enter your operation (+ (addition), - (subtraction), * (multiplication), / (division)): ")

if operation == "+":
    answer = num1 + num2
    print(answer)
elif operation == "-":
    answer = num1 - num2
    print(answer)
elif operation == "*":
    answer = num1 * num2
    print(answer)
elif operation == "/":
    answer = num1 / num2
    print(answer)
else:
    print("error: invalid operation entered")


