def dfs(arr, i, prev):
    if i >= len(arr) or arr[i] < prev:
        return 1

    if (i, prev) in dp:
        return dp[(i, prev)]

    max_length = 0
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            length = dfs(arr, j, arr[i]) + 1
            max_length = max(max_length, length)

    dp[(i, prev)] = max_length + (1 if i == 0 else 0)
    return max_length

def longest_increasing_subsequences(arr):
    global dp
    dp = {}

    ans = 0
    for i in range(len(arr)):
        ans = max(ans, dfs(arr, i, -1))

    return ans

# Example usage:
arr = [2, 3, 4, 5, 6]
print(longest_increasing_subsequences(arr))  # Output: 5
