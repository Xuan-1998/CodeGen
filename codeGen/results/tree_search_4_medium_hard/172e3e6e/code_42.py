import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    mod = 10**9 + 7
    
    dp = [[0]*len(a) for _ in range(n+1)]
    for i in range(len(a)):
        dp[i][i] = 1
    
    for i in range(1, n):
        for j in range(i):
            if a[i]%j==0:
                dp[i][j] = (dp[i-1][j-1] + dp[i][max(j, a[i]//j)])%mod
            else:
                dp[i][j] = 0
    
    print(sum(dp[-1]))%mod

if __name__=="__main__":
    solve()
