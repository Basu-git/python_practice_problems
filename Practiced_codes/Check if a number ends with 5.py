#Check if a number ends with 5.
n=int(input("Enter a number : "))
if n%5==0 and n%10!=0:
    print("number ends with 5")
else: 
    print("No number not ends with 5")