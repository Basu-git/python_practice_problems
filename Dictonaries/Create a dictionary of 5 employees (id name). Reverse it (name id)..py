#4. Create a dictionary of 5 employees (id: name). Reverse it (name: id).
dic={"B":12,"S":13,"A":14,"D":15}
for key,value in dic.items():
    print(f"{value}:{key}",end=",")
print()
#OR
reverse={name:id for id,name in dic.items()}
print(dic)
print(reverse)