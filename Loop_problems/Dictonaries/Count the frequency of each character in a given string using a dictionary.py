#5. Count the frequency of each character in a given string using a dictionary
from collections import Counter
dic="Basavaraj"
print(Counter(dic))

#OR
f={}
for d in dic:
    f[d]=f.get(d,0)+1
print(f)
    