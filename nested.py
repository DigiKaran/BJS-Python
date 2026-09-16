age = int(input("Enter your age: "))
has_id = str(input("Do you have id (True/False)? "))
 
if age >= 18:
    if has_id == "True":
        print("Entry allowed")
    else:
        print("Entry denied: ID required")
else:
    print("Entry denied: Age requirement not met")
