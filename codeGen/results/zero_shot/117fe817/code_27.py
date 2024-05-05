def count_digit_ones(n):
    total_count = 0
    k = 0
    while (1 << k) <= n:
        total_count += k
        k += 1
    return total_count

n = int(input())  # read input from stdin
print(count_digit_ones(n))  # print the result to stdout
