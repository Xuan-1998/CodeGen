def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i - 1] == a[i]:
            dp[i] = max(dp[i], dp[i - 1])
        else:
            dp[i] = max(dp[i], dp[i - 1] + (i > 0) * (a[i] != a[i - 1]))
    
    print(dp[-1])

if __name__ == "__main__":
    solve()
