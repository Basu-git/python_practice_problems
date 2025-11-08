n=input("Enter a word:").lower()
v="aeiou"
c=0
for i in n:
   for j in v:
       if j in i:
           c+=1
        
print(c)