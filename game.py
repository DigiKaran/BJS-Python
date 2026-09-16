amount = int(input("Enter the total amount - "))
if amount >= 10000 :
    print(amount - (amount * 20 / 100))
elif amount >= 5000 :
    print(amount - (amount * 10 / 100))
elif amount >= 2000 :
    print(amount - (amount * 5 / 100))
else :
    print("No discount")