def find_subset(arr, n, m):
    memo = {}

    def dfs(i, s):
        if (i, s) in memo:
            return memo[(i, s)]
        if i == n:
            return 1 if s % m == 0 else 0
        take = dfs(i + 1, s + arr[i]) if arr[i] <= s // m else 0
        not_take = dfs(i + 1, s)
        memo[(i, s)] = take + not_take
        return memo[(i, s)]

    return dfs(0, 0)

# Example usage:
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(find_subset(arr, n, m))
