def max_score(n, k, z, arr):
    # Create a dictionary to store calculated scores
    memo = {(i, j): float('-inf') for i in range(1, n+1) for j in range(k+1)}

    def dp(i, j):
        if i > 0 and j <= k:
            return max(dp(i-1, j-1) + arr[i-1] if j > z else float('-inf'), 
                       dp(i-1, j) + arr[i])
        return arr[i-1] if i == 1 else 0

    # Calculate the maximum score for each subproblem
    max_score = 0
    for i in range(1, n+1):
        for j in range(min(k, i)):
            memo[(i, j)] = dp(i, j)
            max_score = max(max_score, memo[(i, j)])

    return max_score

# Read input from stdin
n, k, z = map(int, input().split())
arr = list(map(int, input().split()))

# Calculate and print the maximum score
print(max_score(n, k, z, arr))
