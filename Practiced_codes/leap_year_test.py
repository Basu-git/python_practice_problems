#Check if a year is a leap year
year=int(input("Enter a Year: "))
if  year%2==0 and year%4==0:
    print("Given year is Leap year")
else:
    print("Given year is not a leap year or enter valid year")