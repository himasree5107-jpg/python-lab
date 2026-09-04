num1 = float(input("Enter the number 1:"))
num2 = float(input("Enter the number 2:"))
op = input("What operation are you going to use: +, -, *, /, **, //, %:")

if op == "**":
    n = num1 ** num2
    print("Power:", n)

elif op == "//":
    n = num1 // num2
    print("Floor division:", n)

elif op == "+":
    n = num1 + num2
    print("Addition:", n)

elif op == "-":
    n = num1 - num2
    print("Subtraction:", n)

elif op == "*":
    n = num1 * num2
    print("Multiplication:", n)

elif op == "/":
    n = num1 / num2
    print("Division:", n)

elif op == "%":
    n = num1 % num2
    print("Remainder:", n)

else:
    print("Error!!!!!!!!!!!!!!!!!")
    
