n=int(input("Enter a number: "))
for i in range(1,n):
    if n%1==0 and n%n==0 and n%2!=0 and n%3!=0 and n%5!=0:
        print(f"{n} is a prime number")
        break
    else:
        print(f"{n} is not a prime number")
        break
print("You got output Right")