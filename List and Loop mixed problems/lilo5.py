#9. Write a program to print a multiplication table (1 to 10) using nested loops and store results in a list
lst=[]
for i in range(1,11):
    row=[]
    for  j in range(1,11):
        row.append(i*j)
    lst.append(row)
for row in lst:
    print(row)
    print()