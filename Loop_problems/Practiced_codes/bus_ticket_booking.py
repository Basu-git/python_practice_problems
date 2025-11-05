seats=8
while seats<=8:
    print(f"Seats availability-{seats}")
    book=input("DO you want to book tickets(yes/no): ").lower()
    
    if book=="yes" and seats!=0:
        seats-=1
        print("Ticket is booked is confirmed")
    else:
        print("Ticket is not booked")
        
print("Either you refused or there is no availability of seats")