import sys

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[False] * (n+2) for _ in range(n+1)]
    
    dp[0][1] = True
    
    for i in range(1, n+1):
        if p[i-1] > 0:
            dp[i][p[i-1]] = dp[i-1][i]
    
    res = 0
    for j in range(2, n+2):
        if dp[0][j]:
            res = (res + 1) % (10**9 + 7)
    
    print(res)

if __name__ == "__main__":
    solve()
