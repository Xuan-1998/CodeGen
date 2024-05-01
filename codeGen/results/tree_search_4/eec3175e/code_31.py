import sys

def can_sum_divisible(n, m, arr):
    memo = [0] * (n + 1)
    total_sum = sum(arr)

    for i in range(1, n + 1):
        current_sum = sum(arr[:i])
        if current_sum % m == 0:
            memo[i] = 1
        else:
            memo[i] = 0

    return memo[-1]

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# Solve the problem and print the answer to stdout
result = can_sum_divisible(n, m, arr)
print(result)
