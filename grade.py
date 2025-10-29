grade=int(input("Enter your Grade: "))
if grade>90 and grade<=100:
    print("Excellent!!!!")
elif grade<=90 and grade>80:
    print("Your grade is A")
elif grade >70 and grade<=80:
    print("Your grade is B")
elif grade>=40 and grade <=70:
    print("Your grade is C")
elif grade<40:
    print("You are failedd!!")
else:
    print("Something error")