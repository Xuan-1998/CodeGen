import sys

def max_points(n, seq):
    dp = [[0] * 105 for _ in range(105)]

    def dfs(i, k):
        if i < 0:
            return 1
        if dp[i][k] > 0:
            return dp[i][k]
        
        if a[k-1] == k or a[k+1] == k:
            points = 1
        else:
            points = 2

        for j in range(i):
            if abs(a[j] - k) == 1:
                continue
            points += dfs(j, a[j])

        dp[i][k] = max(points, 1 + dfs(i-1, a[i-1]))
        return dp[i][k]

    a = [int(x) for x in sys.stdin.readline().split()]
    print(dfs(n-1, a[0]))

