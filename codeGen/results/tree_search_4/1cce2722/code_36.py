from sys import stdin

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i > 1 and a[i-1] == a[i]:
            dp[i] = max(dp[i-1], dp[k] + (k - i) + (n - k) - (a[i] - a[k]) for k in range(i+1, min(i+2, n)))
        else:
            dp[i] = dp[i-1]
    
    return dp[-1]

print(solve())
