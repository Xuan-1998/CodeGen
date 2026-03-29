import sys
from collections import defaultdict

def solve():
    n = int(input())
    m = list(map(int, input().split()))
    
    memo = defaultdict(int)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        for j in range(i, -1, -1):
            if m[i] > m[j]:
                break
            dp[i+1] += dp[j]
            dp[i+1] %= (10**9 + 7)
    
    print(dp[n])

if __name__ == "__main__":
    solve()
