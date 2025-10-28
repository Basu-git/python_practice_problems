m=input("Enter any type of string: ")
n="aeiouAEIOU"
count=0
for char in m:
    if char in n:
        count+=1  
print(f"The number of vowels present in string: {count}") 
    