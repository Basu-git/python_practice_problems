a=int(input("Enter a: "))
b=int(input("Enter b: "))
lcm=max(a,b)
while True:
    if lcm%a==0 and lcm%b==0:
        print(f"Lcm is {lcm}")
        break
    lcm+=1