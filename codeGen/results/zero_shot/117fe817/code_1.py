def count_digit1(n):
    total_count = 0
    for i in range(10):
        total_count += min(i+1, n//10**(9-i)) * (1 << (9 - i))
    return total_count
