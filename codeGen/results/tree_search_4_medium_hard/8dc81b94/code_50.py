def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[n] = True
    
    for i in range(n - 1, -1, -1):
        if arr[i] % 2 == 0:
            dp[i] = dp[i + 1]
        else:
            dp[i] = (dp[i + 1] or dp[n])
    
    print("YES" if dp[0] else "NO")

if __name__ == "__main__":
    solve()
