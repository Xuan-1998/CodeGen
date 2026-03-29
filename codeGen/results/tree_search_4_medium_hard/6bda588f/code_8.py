import sys
from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[sys.maxsize] * (s + 1) for _ in range(n + 1)]
        dp_prev = defaultdict(lambda: sys.maxsize)
        
        for i in range(1, n + 1):
            for j in range(s + 1):
                if j >= a[i - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - a[i - 1]] + a[i - 1])
                else:
                    dp[i][j] = dp_prev[j]
                
                dp_prev[j] = min(dp_prev[j], dp[i][j])
        
        print(min(dp[-1]))

if __name__ == "__main__":
    solve()
