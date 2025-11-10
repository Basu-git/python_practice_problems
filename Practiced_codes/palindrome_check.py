word=input("Enter a word to check for palindrome: ")
if word==word[::-1]:
    print(f"{word} is a palindrome")#True
else:
    print(f"{word} is not a palindrome")#False