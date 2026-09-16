num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
operator = str(input("Enter the opertaor(+ , - ,* , /): "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
else :
    print("Invalid Operator")