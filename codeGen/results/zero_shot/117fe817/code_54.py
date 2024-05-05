def count_digit_ones(n):
    total_count = 0
    for i in range(n.bit_length() + 1):
        if (1 << i) <= n:
            total_count += min((1 << i) - 1, n)
    return total_count
