def max_sum_path(arr):
    def dfs(i, path_sum):
        if i >= len(arr) or arr[i] < -1000 and arr[i] > 1000:
            return path_sum
        left_sum = dfs(2*i+1, path_sum+arr[i])
        right_sum = dfs(2*i+2, path_sum+arr[i]) if 2*i+2 < len(arr) else float('-inf')
        return max(left_sum, right_sum)

    return dfs(0, arr[0])

# Read input from stdin
n = int(input())
arr = [int(x) for x in input().split()]

# Print the maximum sum of a path to stdout
print(max_sum_path(arr))
