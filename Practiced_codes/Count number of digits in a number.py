#Count number of digits in a number
n=int(input("Enter num : "))
sum=0
while n>0:
    num=n%10
    sum+=1
    n=n//10

print(sum)