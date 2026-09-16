income = int(input("Enter your income: "))
if income > 1000000:
    print(income + (income * 30 / 100))
elif income > 500000:
    print(income + (income * 20 / 100))
elif income > 250000:
    print(income + (income * 5 / 100))
else:
    print("No tax applied")