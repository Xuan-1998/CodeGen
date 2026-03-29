def count_digit_ones(n):
    total = 0
    for i in range(1, n + 1):
        total += str(i).count('1')
    return total

n = int(input())  # receive input from stdin
print(count_digit_ones(n))  # print the result to stdout
