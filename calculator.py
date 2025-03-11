def calculator():
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")
    operator = input("enter the operator (+, -, *, /): ")
    if operator == "+":
        print(int(num1) + int(num2))
    elif operator == "-":
        print(int(num1) - int(num2))
    elif operator == "*":
        print(int(num1) * int(num2))
    elif operator == "/":
        print(int(num1) / int(num2))
    else:
        print("invalid operator")
if __name__ == "__main__":
    calculator()