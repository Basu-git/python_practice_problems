#### 29. Count Words (Easy)
#**Description:** Count words separated by spaces in a sentence.
#**Example Input:** This is fun
#**Expected Output (blueprint):** 3
n=input("Enter a Sentence: ")
count=0
for i in n:
    if i==" ":
        continue
        count+=1 
print(count)       