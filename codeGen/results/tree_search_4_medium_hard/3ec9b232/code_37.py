import sys

def solve():
    n = int(input())
    M = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = {}
    def dfs(i):
        if (i, ) in dp:
            return dp[(i, )]
        if i == 0:
            return 1
        
        res = 0
        for k in range(i+1):
            if M[k-1] < M[i]:
                res += dfs(k-1)
                res %= MOD
        dp[(i, )] = res + 1
        return dp[(i, )]
    
    print(dfs(n-1) % MOD)

if __name__ == "__main__":
    solve()
