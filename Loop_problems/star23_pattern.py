#***
#* *
#***
# Hollow square pattern
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
