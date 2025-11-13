#### 22. Sum Even Numbers (Easy)
#**Description:** Sum only even numbers in a list.
#**Example Input:** [1,2,3,4,5]
#**Expected Output (blueprint):**
n=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in n:
    if i%2==0:
        sum+=i
   
print(sum)