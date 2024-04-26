import math

def count_perfect_squares(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if i ** 2 <= n:
            count += 1
    return count

n = int(input())  # read input from stdin
print(count_perfect_squares(n))  # print the result to stdout
