#### 43. Remove Duplicates (sorted) (Medium)
#**Description:** Remove duplicates from sorted list.
#**Example Input:** [1,1,2,3,3]
#**Expected Output (blueprint):** [1,2,3]
n=list(input("Enter a numbers : "))
print(sorted(list(set(n))))