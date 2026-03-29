import sys

def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i-1][j-1] * int(input()) if i <= j else 0, 
                               dp[i-1][j])
    
    res = []
    i, j = n, k
    while j > 0 and i > 0:
        if dp[i][j] != dp[i-1][j]:
            res.append((i, j))
            i -= 1
            j -= 1
        else:
            i -= 1
    
    print(*res)
    print(dp[n][k])

if __name__ == "__main__":
    solve()
