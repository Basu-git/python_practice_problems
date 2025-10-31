n=input("Enter a numbber: ")
c=[int(d) for d in str(n)]
p=len(n)
if sum(d**p for d in c)==n:
    print("Armstrong Number")
else:
    print("Not Armstrong number")