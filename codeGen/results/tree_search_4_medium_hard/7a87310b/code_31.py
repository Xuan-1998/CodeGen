import sys
from collections import defaultdict

def count_matrices():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(3, n+1):
            for j in range(-n, n+1):
                if i <= 0 or j == 0:
                    continue
                if j - 1 >= 0 and dp[i-2][j-1]:
                    dp[i][j] += dp[i-2][j-1]
                if j + 1 <= n and dp[i-2][j+1]:
                    dp[i][j] += dp[i-2][j+1]
        print(sum(1 for i in range(n//2, -n//2) if (n - i*2) % 2 == 0 and dp[n-i*2][i]))

count_matrices()
