def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * 2 for _ in range(n + 1)]
    
    dp[0][0] = True
    
    for i in range(1, n + 1):
        if arr[i - 1] == 0:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][1] or dp[i - 1][0]
        dp[i][1] = dp[i - 1][0] and arr[i - 1] == 0
    
    if dp[n][0]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
