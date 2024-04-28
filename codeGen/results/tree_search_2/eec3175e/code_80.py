def can_sum_divisible_by_m(n, m, arr):
    memo = {}

    def dfs(i, target):
        if i >= n or target < 0:
            return False
        if (i, target) in memo:
            return memo[(i, target)]
        if target == 0:
            return True

        if arr[i] > target:
            result = dfs(i + 1, target)
        else:
            result = dfs(i + 1, target - arr[i]) or dfs(i + 1, target)

        memo[(i, target)] = result
        return result

    for i in range(n):
        if dfs(i, m) is True:
            return 1
    return 0
