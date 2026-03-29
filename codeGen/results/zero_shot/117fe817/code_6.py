def count_digit_ones(n):
    count = 0
    for i in range(n + 1):
        count += bin(i).count('1')
    return count

n = int(input())  # read input from stdin
print(count_digit_ones(n))  # print the result to stdout
