def count_ones(n):
    total_ones = 0
    for i in range(1, n + 1):
        ones_in_current_integer = str(i).count('1')
        total_ones += ones_in_current_integer
    return total_ones
