room = input("Enter room type (Standard/Deluxe/Suite): ")
days = int(input("Enter number of days: "))
member = input("Are you a member? (Yes/No): ")

if room == "Standard":
    price = 2000 * days

    if member == "Yes":
        discount = price * 10 / 100
    else:
        discount = 0

elif room == "Deluxe":
    price = 3500 * days

    if member == "Yes":
        discount = price * 15 / 100
    else:
        discount = 0

elif room == "Suite":
    price = 5000 * days

    if member == "Yes":
        discount = price * 20 / 100
    else:
        discount = 0
else:
    print("Invalid room type")
    price = 0
    discount = 0

final_price = price - discount

print("Base Price:", price)
print("Discount:", discount)
print("Final Price:", final_price)