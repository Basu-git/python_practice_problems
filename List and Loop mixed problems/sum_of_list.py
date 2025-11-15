#### 48. Sum of Two Lists (element-wise) (Medium)
#**Description:** Add two lists element-wise.
##**Example Input:** [1,2,3] and [4,5,6]
#**Expected Output (blueprint):** [5,7,9]
l1=[1,2,3]
l2=[4,5,6]
sum=[]
for i in range(len(l1)):
    sum.append(l1[i]+l2[i])
print(sum)
