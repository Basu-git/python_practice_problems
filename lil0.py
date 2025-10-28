#10. Create a list of integers and use a loop to remove all odd numbers from the list.
lst=[]
lst2=[1,2,3,4,5,6,7,8,9]
for i in range(1,50):
    if i%2==0:
        lst.append(i)
print(lst)
for l in lst2:
    if l%2!=0:
        lst2.remove(l)
print(lst2)