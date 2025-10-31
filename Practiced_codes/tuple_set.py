l=["basu","shreya","anirudha",2]
print(l)
b=set(l)
print(set(b))#print in unordered because sets are unodrdered
b.add(799999)#Adds 7 to the set at a random order
print(b)
print(tuple(l))
tuple(l).add(7)#prints error because tuples are immutable
print(tuple(l))
