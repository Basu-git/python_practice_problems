def count_digits():
    if n == 0:
        return 1  # Special case: 0 has 1 digit

    count = 0
    n = abs(n)  # In case the number is negative

    while n > 0:
        n //= 10
        count += 1

    return count
