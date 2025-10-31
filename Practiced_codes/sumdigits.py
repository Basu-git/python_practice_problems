n=input("Enter a numbers: ")
c=0
for d in n:
    c=c+int(d)
print(c)
#or
num=input("Enter numbers: ")
print(sum(int(d) for d in num))