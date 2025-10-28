#6. Merge two dictionaries into one. If a key repeats, add the values
dic1={"B":12,"A":12}
dic2={"B":12}
m=dic1.copy()
for k,v in dic2.items():
    m[k]=m.get(k,0)+v
print(m)