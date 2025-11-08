fruits = ['apple', 'banana', 'mango', 'cherry', 'banana', 'apple']
c=list(set(fruits))
for fruit in fruits:
    a=fruits.count(fruit)
    print(a)
print(c)