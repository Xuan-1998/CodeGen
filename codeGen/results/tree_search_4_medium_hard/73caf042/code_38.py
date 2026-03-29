import sys

def get_sum_of_digits(n):
    even_sum = 0
    odd_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        n //= 10
    return abs(even_sum - odd_sum)

def dp(i, j):
    if i < 1 or j < 1:
        return 0
    memo = [[0] * (j + 1) for _ in range(i + 1)]
    for k in range(1, i + 1):
        for l in range(1, j + 1):
            if k == 1 and l == 1:
                memo[k][l] = get_sum_of_digits(k + l - 1)
            else:
                memo[k][l] = dp(k - 1, l - 1) + abs(get_sum_of_digits(k + l - 1))
    return memo[i][j]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp(N, N))
