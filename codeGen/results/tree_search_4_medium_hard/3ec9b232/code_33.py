def mergeable_ways(n):
    M = list(map(int, input().split()))
    memo = {}

    def dfs(i, j, used):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == j:
            return 1 if all(M[k] < M[i] for k in range(i)) else 0
        used_val = used.get(M[i], 0)
        used[M[i]] = used_val + 1
        ans = 0
        for k in range(i):
            if M[k] <= M[i]:
                ans += dfs(k, i - 1, used)
            else:
                ans += sum(dfs(l, i - 1, used) for l in range(k+1, i))
        used[M[i]] = used_val
        return (ans + 1) % (10**9 + 7)

    return dfs(0, n-1, {})

print(mergeable_ways(int(input())))
