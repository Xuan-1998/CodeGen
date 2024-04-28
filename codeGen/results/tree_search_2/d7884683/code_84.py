def max_partitions(arr):
    n = len(arr)
    total_sum = sum(arr)

    @lru_cache(None)
    def dfs(left_sum, right_sum, left_index):
        if left_index >= n:
            return 0

        result = 0
        for i in range(left_index, n):
            new_left_sum = left_sum + arr[i]
            new_right_sum = total_sum - new_left_sum
            if (new_left_sum, new_right_sum) in memo:
                result = max(result, dfs(new_left_sum, new_right_sum, i+1) + 1)
            else:
                result = max(result, dfs(new_left_sum, new_right_sum, i+1))
        return result

    if n % 2 != 0:
        return dfs(0, total_sum, 0)

    memo = {(arr[0], arr[-1]): 1}
    return dfs(arr[0], arr[-1], 1)
