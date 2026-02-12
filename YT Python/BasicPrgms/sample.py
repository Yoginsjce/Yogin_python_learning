pin="2402"
trials=1
while trials<=3:
    trials+=1
    input_pin=(input("Enter the pin >>"))
    if input_pin==pin:
        print("SUCCESS")
        break
    else:
        print("WRONG PIN TRY AGAIN")