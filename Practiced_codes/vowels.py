a=input("Enter letters: ").lower()
v="aeiou"
count=0
for ch in a:
    if ch in v:
        count+=1
print(count)
#or
ch=input("Enter letters: ").lower()
v="aeiou"
print(sum(1 for c in ch if c in v))