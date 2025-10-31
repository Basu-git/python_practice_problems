def first(n):
    if n==1:
        return 1
    return n+first(n-1)

print(first(8))