#7. Take input of 5 numbers from the user, store in a list, and use a loop to find the average.
num=[]
for i in range(5):
    n=int(input(f"Enter number {i+1}: "))
    num.append(n)
print(f"The list is {num}")
print(f"The Average is  {(sum(num)/len(num))}")
