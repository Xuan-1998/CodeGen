def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * 2 for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for k in range(2):
            if (arr[i - 1] % 2 == 0 and k == 0) or (arr[i - 1] % 2 != 0 and k == 1):
                dp[i][k] = (i == 1 or dp[i - 1][k])
    
    print("YES" if dp[n][0] else "NO")

if __name__ == "__main__":
    solve()
