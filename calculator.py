def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result:", add(num1, num2))
    elif op == "-":
        print("Result:", subtract(num1, num2))
    elif op == "*":
        print("Result:", multiply(num1, num2))
    elif op == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation!")

calculator()