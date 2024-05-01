from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    memo = defaultdict(lambda: defaultdict(int))
    dp = [[0] * 107 for _ in range(n+1)]

    def dfs(i, k):
        if i == -1:
            return 0
        if dp[i][k] > 0:
            return dp[i][k]
        
        res = 0
        for j in range(i):
            if abs(a[j]-k) == 1:
                res = max(res, dfs(j-1, a[j]))
            else:
                res = max(res, dfs(j, a[j]))
        dp[i][k] = res + 1
        return dp[i][k]

    print(dfs(n, a[0]))

if __name__ == "__main__":
    solve()
