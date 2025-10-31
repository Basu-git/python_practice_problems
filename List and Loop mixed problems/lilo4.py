#8. Given numbers = [5,2,9,1,5,6]: Use a loop to count how many times the number 5 appears
numbers = [5,2,9,1,5,6]
c=0
for n in numbers:
    if n==5:
        c+=1
print(f"The number 5 appeared {c} times")