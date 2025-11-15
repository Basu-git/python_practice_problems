#### 59. Spiral Matrix Print (Medium)
#**Description:** Print elements of matrix in spiral order.
#**Example Input:** [[1,2,3],[4,5,6],[7,8,9]]
#**Expected Output (blueprint):** 1 2 3 6 9 8 7 4 5
n=[[1,2,3],[4,5,6],[7,8,9]]
for i in n:
    for j in i:
        print(j,end=" ")