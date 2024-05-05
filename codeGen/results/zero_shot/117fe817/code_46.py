def count_digit_ones(n):
    total_ones = 0
    for i in range(10**9 // 10 + 1):
        ones_in_i = min((i + 1) % 10, (i + 2) % 10, (i + 3) % 10)
        if ones_in_i == 1:
            total_ones += (10**i - i - 1) // 9 * 3 + 1
    return total_ones

n = int(input())
print(count_digit_ones(n))
