def can_cross_stones(stones):
    n = len(stones)
    memo = {}

    def dfs(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i == n - 1:  # base case: reached the end of the river
            return True
        if k <= 0:  # edge case: frog cannot jump backwards
            return False

        next_stone = stones[i + 1]
        if abs(next_stone - stones[i]) not in [k - 1, k, k + 1]:  # invalid jump
            return False

        memo[(i, k)] = any(dfs(i + 1, j) for j in range(max(0, next_stone - k), min(n - 1, next_stone + k + 1)))
        return memo[(i, k)]

    return dfs(0, 0)
