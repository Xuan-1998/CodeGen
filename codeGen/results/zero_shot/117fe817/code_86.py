def count_digit_ones(n):
    total = 0
    for i in range(n + 1):
        if '1' in str(i):
            total += 1
    return total

n = int(input())  # read input from stdin
print(count_digit_ones(n))  # print output to stdout
