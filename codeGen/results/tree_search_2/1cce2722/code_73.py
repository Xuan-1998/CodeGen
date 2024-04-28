def delete_points(a):
    n = len(a)
    dp = [0] * (n + 1)

    def dfs(i):
        if i > 0:
            if dp[i] == 0:
                dp[i] = max(dfs(j-1) + (a[i] - 1) if a[i] % 2 == 0 else 1 for j in range(1, i+1))
            return dp[i]
        return 0

    return dfs(n)

n = int(input())
a = list(map(int, input().split()))
print(delete_points(a))
