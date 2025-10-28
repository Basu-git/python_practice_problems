#9. Given a dictionary, sort it by keys and values separately.
dic={"B":12,"S":13,"A":14,"D":15}
print(dic)
print("By Keys",sorted(dic.keys()))
print("By values",sorted(dic.values()))
print("By key based on value",sorted(dic.items(),key=lambda x:x[1]))