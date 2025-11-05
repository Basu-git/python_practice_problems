#3. Write a program to check if a given key exists in a dictionary. If not, insert it with a default value
dic={"B":12,"S":13,"A":14,"D":15}
n=input("Enter key you want to find: ").upper()
if n in dic:
    print(f"{n}:{dic[n]} is found in dic")
else:
    print("Not Found!!!")