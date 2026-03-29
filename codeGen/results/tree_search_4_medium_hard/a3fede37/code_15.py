def maxPathSum(root):
    memo = {0: 0}
    max_sum = float('-inf')

    def dfs(node):
        if node not in memo:
            val = node[1]
            left_sum = right_sum = 0

            if node[0] * 2 + 1 in memo:
                left_sum = memo[node[0] * 2 + 1]
            if node[0] * 2 in memo:
                right_sum = memo[node[0] * 2]

            memo[node] = val + max(left_sum, right_sum)
            nonlocal max_sum
            max_sum = max(max_sum, memo[node])
        return memo[node]

    dfs((1, root))
    return max_sum


# Example usage:
root = [4, 9, 0, 0, 5, 0, 0, None, None]
print(maxPathSum(root))  # Output: 22
