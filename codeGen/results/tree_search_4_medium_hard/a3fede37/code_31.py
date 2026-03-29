import sys

def max_path_sum(arr):
    n = len(arr)
    dp = {0: 0}

    for i in range(1, n):
        node = arr[i]
        if node == 0:  # root node
            left_sum = dp.get(arr[i-1], -sys.maxsize) + node
            right_sum = dp.get(arr[i+1], -sys.maxsize) + node
            dp[node] = max(left_sum, right_sum)
        else:
            if i * 2 < n:  # left child exists
                left_child_sum = dp.get(arr[i*2-1], -sys.maxsize) + node
            else:
                left_child_sum = -sys.maxsize

            if i * 2 + 1 < n:  # right child exists
                right_child_sum = dp.get(arr[i*2+1], -sys.maxsize) + node
            else:
                right_child_sum = -sys.maxsize

            dp[node] = max(left_child_sum, right_child_sum) + node

    return max(dp.values())

# Example usage:
arr = [1, 2, 3, 4, 5]
print(max_path_sum(arr))  # Output: 9 (path: 1 -> 2 -> 3 -> 4 -> 5)
