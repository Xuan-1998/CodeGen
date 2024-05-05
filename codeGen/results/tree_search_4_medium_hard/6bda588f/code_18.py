import sys

def min_f(a, n, s):
    dp = [[0] * (2*s + 1) for _ in range(n)]
    prev_sum = [0] * (2*s + 1)

    def dfs(i, s):
        if i == n:
            return 0
        if dp[i][s]:
            return dp[i][s]
        
        res = float('inf')
        for x in range(s // a[i] + 1):
            y = s - a[i] * x
            res = min(res, dfs(i + 1, y) + a[i] * x)
            prev_sum[s] = a[i]

        dp[i][s] = res
        return res

    return dfs(0, s)


t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a, n, s))
