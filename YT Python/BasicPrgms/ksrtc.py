available_seats=5
while available_seats>0:
    print(f"The available seats are {available_seats}")
    booking=input("Do you want to book the seat (Y/N): ")
    if booking=="Y":
        print("Seat Booked")
        print("Happy journey.....")
        available_seats-=1
    else:
        print("Seat not Booked")
print("All seats booked...")
print(f"the available seats are {available_seats}")