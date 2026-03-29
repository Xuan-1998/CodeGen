import sys

def count_digit_ones(n):
    total_count = 0
    for i in range(1, 10):  # iterate over each possible value of the ones place
        if i <= n:  # only consider numbers with 1 as their most significant digit
            total_count += n // i + 1  # count the number of times 1 appears in that position
    return total_count

n = int(sys.stdin.readline())
print(count_digit_ones(n))
