#conditional statements programs
gender=input("Enter your gender: ")

if gender=="female":
    print("Ticket is free...")
else:
    age=int(input("Enter your age: "))
    if age<=5:
        print("free ticket:..")
    elif age<=12:
        print("Child ticket price")
    elif age>60:
        print("Senior citizen")
    else:
        print("full ticket ")
