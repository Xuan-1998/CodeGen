import sys

def count_good_subsequences(n, a):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if a[j] % (j + 1) == 0:
                dp[i] += dp[j]
    return sum(dp) % (10**9 + 7)

n = int(input())
a = [int(x) for x in input().split()]
print(count_good_subsequences(n, a))
