def findPaths(N, K, arr):
    # Create a memoization table to store previously computed values
    memo = {}

    def dfs(i, j, k):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == N-1 and j == N-1:
            return 1 if k == K else 0

        total_coins = arr[i][j]
        if k < total_coins or i > 0 and j > 0:
            return 0

        ways = dfs(i+1, j, k) + dfs(i, j+1, k)
        memo[(i, j)] = ways
        return ways

    # Start the DFS from the top-left corner (0, 0) with K coins
    return dfs(0, 0, K)

# Example usage:
N = int(input())  # Read N from standard input
K = int(input())  # Read K from standard input
arr = [[int(x) for x in input().split()] for _ in range(N)]  # Read the 2D matrix arr[][]

print(findPaths(N, K, arr))  # Print the result
