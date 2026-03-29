def min_cost_to_sort_strings(n, costs, strings):
    memo = {}

    def dfs(i, s):
        if (i, s) in memo:
            return memo[(i, s)]
        if i == n:
            return 0

        ans = float('inf')
        for j in range(len(strings[i])):
            new_s = s + strings[i][j:]
            if new_s not in s:
                ans = min(ans, dfs(i+1, new_s) + costs[i])
        memo[(i, s)] = ans
        return ans

    return dfs(0, "")
