import sys

def solve():
    T = int(input())
    dp = [[-1 for _ in range(10001)] for _ in range(10001)]
    
    def dfs(i, j):
        if i == 0:
            return (j + M - 2) % X
        if dp[i][j] != -1:
            return dp[i][j]
        
        res = (dfs(i-1, (j+M-2)%X)) % X
        
        if res == j:
            res = (res+1) % X
            
        dp[i][j] = res
        return res

    for _ in range(T):
        M, X = map(int, input().split())
        result = [0 for _ in range(X+1)]
        
        for i in range(1, X+1):
            result[i] = dfs(i, 0) + 1
            
        print(*result[1:])

if __name__ == "__main__":
    solve()
