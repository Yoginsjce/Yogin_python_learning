# available_seats=5
# while available_seats>0:
#     seat_book=input(f"Do you want to book seats,yes/NO >> ")
#     if seat_book=="yes":
#         available_seats-=1
#         print(f"Seat Booked,Now available_seats are {available_seats}")
#     else:
#         print(f"Seat Not booked available seats are {available_seats}")    
# print("All seats are booked")

snacks=3
money=10
while money>0 and snacks>0:
    print("Do you want to purchase chips ?? ")
    purchase=input("Yes/No ->> ")
    if purchase=="yes" and money>=5:
        snacks-=1
        money-=5
        print(f"Item Purchased remaining balance is {money} and snacks stock is {snacks}")
    else:
        print("Not Purchased")
print("Either you dont have money or snacks")