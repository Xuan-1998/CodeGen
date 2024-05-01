import sys

def min_falling_path_sum(A):
    m = len(A)
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return A[i][j]
        min_sum = float('inf')
        for k in range(m):
            if k != j:
                min_sum = min(min_sum, dfs(i-1, k) + A[i][j])
        memo[(i, j)] = min_sum
        return min_sum

    return dfs(m-1, 0)

# Example usage
A = [[1,2,3], [5,6,9], [4,7,8]]
print(min_falling_path_sum(A))  # Output: 13
