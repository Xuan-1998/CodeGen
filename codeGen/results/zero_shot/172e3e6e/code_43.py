import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        if a[i - 1] % i:
            continue
        for j in range(i, n + 1):
            if not a[j - 1] % j or dp[i-1][j-1]:
                dp[i][j] = True
    
    ans = 0
    for i in range(1, n + 1):
        if dp[n][i]:
            ans += 1
    print(ans % (10**9 + 7))

solve()
