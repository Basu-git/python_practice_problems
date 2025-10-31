a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if(a>10 and b>10):
    print("Both numbers are greater than 10")
elif(a>5 or b>5):
    print("At least one of the number is greater than 5")
elif(a<b):
    print("The first number is  not greater than second")