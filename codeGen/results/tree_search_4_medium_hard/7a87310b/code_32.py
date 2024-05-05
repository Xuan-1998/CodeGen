import sys

def count_matrices(n):
    dp = {0: 0, 1: 2}
    
    for i in range(2, n + 1):
        dp[i] = 0
        for j in range(i - 1, 0, -1):
            if (i - j) * j > 0:
                dp[i] += dp[j] * (i - j)
    
    return dp[n]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(count_matrices(n))
