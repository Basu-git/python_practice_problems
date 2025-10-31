#3. Write a program to find the maximum number in a list using a loop (do not use max()).
lst=[1,2,34,23,45,6,444,543,567,232321,23213443124,00]
max=lst[0]
for i in lst:
    if i>max:
        max=i
print(max)