import sys

def solve():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n, k, z = map(int, sys.stdin.readline().strip().split())
        
        arr = list(map(int, sys.stdin.readline().strip().split()))
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        dp[0][0] = arr[0]
        
        for i in range(1, n):
            for j in range(min(i, k)):
                if j < z:
                    dp[i][j] = max(dp[i-1][j-1] + arr[i-1], dp[i-1][j] + arr[i])
                else:
                    dp[i][j] = dp[i-1][j-1] + arr[i]
        
        print(max(dp[-1]))

solve()
