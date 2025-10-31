n = int(input("Rows: ")) 
for i in range(n): 
    print(" " * (n - i - 1) + "*" * (2 * i + 1)) 
#      *
#     ***
#    *****
#   *******
#  *********
# ***********