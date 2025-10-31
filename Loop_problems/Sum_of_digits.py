num=int(input("ENter a number: "))
num1=num
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print(sum)