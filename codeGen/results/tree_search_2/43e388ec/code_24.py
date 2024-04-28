import sys

memo = {}

def solve(a, b):
    if (a & b) not in memo:
        result = 0
        for i in range(314159):
            left_shifted_b = b << i
            result += a ^ left_shifted_b
        memo[(a & b)] = result % (10**9 + 7)
    return memo[(a & b)]

a, b = map(int, input().split())
print(solve(a, b))
