#### 9. Simple Interest (Easy)
#**Description:** Given P, R, T, compute simple interest = P*R*T/100.
#*Example Input:** P=1000 R=5 T=2
#**Expected Output (blueprint):** 100
p=int(input("Enter a principal amt: "))
r=int(input("Enter a rate of intrest: "))
t=int(input("Enter duration(in years): "))
amt=(p*r*t)/100
print(f"The amt after simple intrest is {amt}")
