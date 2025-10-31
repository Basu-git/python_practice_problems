#Create a list of 10 numbers. Use a loop to print all even numbers from the list.
lst=list(input("Enter only 10 numbers: "))
print(lst)
even=[int(n) for n in lst if int(n)%2==0]
print(even)