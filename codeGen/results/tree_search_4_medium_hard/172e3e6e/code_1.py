from collections import defaultdict
import sys

MOD = 10**9 + 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        else:
            for j in range(2, i+1):
                if a[i-1] % j == 0:
                    dp[i] += dp[i-1]
                    dp[i] %= MOD
    
    print(dp[-1])

if __name__ == "__main__":
    solve()
