def count_digit_ones(n):
    total = 0
    for i in range(1, 10):
        total += min(i, n) - (i-1)
    return total

n = int(input())  # read input from stdin
print(count_digit_ones(n))  # print the result to stdout
