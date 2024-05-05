import sys

def count_digit_ones(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        if k >= 10:  # handle cases where k has two digits or more
            ones_in_k = (k // 10) + (k % 10)
        else:
            ones_in_k = k
        dp[k] = dp[k - 1] + ones_in_k
    return dp[n]

n = int(sys.stdin.readline())
print(count_digit_ones(n))
