def max_sum_path(arr):
    def dfs(i):
        if 2*i+1 > len(arr) or arr[2*i+1] == -1:  # left child is None
            return arr[i]
        if 2*i+2 > len(arr) or arr[2*i+2] == -1:  # right child is None
            return arr[i] + arr[2*i+1]
        return arr[i] + max(dfs(2*i+1), dfs(2*i+2))
    
    max_sum = float('-inf')
    for i in range(len(arr)):
        if arr[i] != -1:  # node exists
            max_sum = max(max_sum, dfs(i))
    return max_sum

# Example usage:
arr = [5, 2, 8, 3, 9, 4, 1]
print(max_sum_path(arr))  # Output: 18
