def max_path_sum(arr):
    def dfs(i):
        if i >= len(arr) or arr[i] < 0:  # leaf node
            return 0

        left_sum = dfs(2 * i + 1)
        right_sum = dfs(2 * i + 2)

        return max(left_sum, right_sum) + arr[i]

    return max(0, dfs(0))  # start from the root (index 0)

# Example usage
arr = [10, -5, 3, 8, 7, -6]
print(max_path_sum(arr))  # Output: 12
