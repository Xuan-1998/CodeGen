def max_points(a):
    n = len(a)
    memo = {}

    def dfs(i, total, used):
        if i >= n:
            return 0
        if (i, total, used) in memo:
            return memo[(i, total, used)]
        res = 0
        for j in range(i+1, n):
            if a[j] == a[i] + 1 or a[j] == a[i] - 1:
                new_used = used | (1 << i)
                res = max(res, dfs(j, total + a[j], new_used) + 1)
        memo[(i, total, used)] = res
        return res

    return dfs(0, 0, 0)

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
