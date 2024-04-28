from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    memo = defaultdict(int)
    
    for i in range(2, n):
        if a[i] % 2 == 0:
            dp[i] = max(dp[i-1], dp[i-2]) + (a[i] - 1) // 2
        else:
            dp[i] = max(dp[i-1], memo[i-1])
        memo[i] = dp[i]
    
    print(max(dp[n-1], memo[n-1]))

if __name__ == "__main__":
    solve()
