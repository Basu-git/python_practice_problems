#### 19. Remove Spaces (Easy)
#**Description:** Remove all spaces from input string.
#**Example Input:** a b c
#**Expected Output (blueprint):** abc
n=input("Enter a Word: ")
for i in n:
    if i==" ":
        continue
    print(i,end="")