number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
number3 = int(input("Enter the number 3: "))

if number1 >= number2 and number1 >= number3:
    print(f"{number1} is the greatest.")
elif number2 >= number1 and number2 >= number3:
    print(f"{number2} is the greatest.") 
elif number3 >= number1 and number3 >= number2:
    print(f"{number3} is the greatest.")
else:
    print("Invalid input.")
