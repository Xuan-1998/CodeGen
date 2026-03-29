def count_digit_ones(n):
    total_count = 0
    for i in range(n + 1):
        total_count += i // 10 + 1
    return total_count

n = int(input())
print(count_digit_ones(n))
