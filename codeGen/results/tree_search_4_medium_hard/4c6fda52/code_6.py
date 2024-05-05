import sys
from collections import defaultdict

def solve():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(k - 1, n):
            for c in range(min(k - 1, i - k + 2), -1, -1):
                if s[i - k + 1:i + 1] in ['RGBRGBRGB' * (i // k + 1)][0]:
                    dp[i][c] = min(dp[i - 1][c], 1 + dp[i - 1][c - 1])
                else:
                    dp[i][c] = 1 + dp[i - 1][c]
        
        print(min(dp[n - 1]))

if __name__ == '__main__':
    solve()
