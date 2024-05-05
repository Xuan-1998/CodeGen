import sys

def solve():
    t = int(input())
    dp = [[0 for _ in range(2001)] for _ in range(2001)]
    
    def dfs(i, j):
        if i == 1:
            return 1
        if dp[i][j]:
            return dp[i][j]
        
        res = 0
        for k in range(j+1):
            if k >= M and j > i-1:
                break
            res += dfs(i-1, k)
        dp[i][j] = res
        return res
    
    for _ in range(t):
        n, m = map(int, input().split())
        print((dfs(n, m)) % 1000000000)

if __name__ == "__main__":
    solve()
