data = [[1,2,3], [4,5], [6,7,8,9]]
flat=[]
for d in data:
    for a in d:
        flat.append(a)
print(flat)
print([a for d in data for a in d])
