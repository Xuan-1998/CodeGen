import sys
from math import ceil, log10

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        if n > 10**9:
            print(-1)
            continue
        
        dp = [[0] * (m + 1) for _ in range(11)]
        
        for i in range(1, 11):
            dp[i][0] = i
        
        for j in range(m + 1):
            for i in range(9, 0, -1):
                if j < ceil(log10(i)):
                    dp[i][j] = min(dp[i-1][j], i) if j > 0 else i
                else:
                    dp[i][j] = min(dp[i-1][j-ceil(log10(i))], i)
        
        print(dp[n][m])

if __name__ == "__main__":
    solve()
