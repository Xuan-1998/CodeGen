def max_path_sum(arr):
    n = len(arr)
    max_sum = float('-inf')

    def dfs(i, current_sum=0):
        nonlocal max_sum
        if i >= n or arr[i] is None:
            return

        current_sum += arr[i]
        left_sum = dfs(2*i+1, current_sum) if 2*i+1 < n and arr[2*i+1] else 0
        right_sum = dfs(2*i+2, current_sum) if 2*i+2 < n and arr[2*i+2] else 0

        max_sum = max(max_sum, current_sum + left_sum + right_sum)
        return current_sum

    dfs(0)
    return max_sum
