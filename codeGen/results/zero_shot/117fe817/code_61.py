def count_digit_ones(n):
    total = 0
    for i in range(1, n + 1):
        ones_count = len(str(i).replace('0', ''))
        total += ones_count
    return total

n = int(input())
print(count_digit_ones(n))
