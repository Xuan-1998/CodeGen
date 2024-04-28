import sys
input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(m):
        for j in range(n, -1, -1):
            if a[i] <= j:
                dp[j] += dp[j-a[i]]
    
    print(dp[n]%1000000007)

solve()
