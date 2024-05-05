def min_remove_signs(arr, queries):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    def dfs(i, sum_):
        if i > n or sum_ == 0:
            return 0
        if dp[i][sum_] != -1:
            return dp[i][sum_]
        res = float('inf')
        if l <= i and i <= r:
            res = min(res, dfs(i - 1, sum_ + arr[i]))
        dp[i][sum_] = res + (sum_ > 0)
        return dp[i][sum_]

    for query in queries:
        l, r = query
        print(dfs(r, sum(arr[l:r+1])))

# Example usage:
arr = input().split()
queries = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    queries.append((l, r))
min_remove_signs(arr, queries)
