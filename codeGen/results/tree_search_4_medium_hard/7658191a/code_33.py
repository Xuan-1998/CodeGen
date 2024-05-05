def max_score(array, k, z):
    n = len(array)
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # Initialize the first row with values from the input array
    for i in range(1, n+1):
        dp[i][0] = array[i-1]

    # Fill up the dynamic programming table
    for j in range(1, k+1):
        max_score = 0
        for i in range(max(j-z, 0), min(i+j, n)+1):
            score = dp[i-1][j-1] + array[i-1]
            if score > max_score:
                max_score = score
                prev_index = i - 1
        dp[prev_index][j] = max_score

    # Find the maximum score in the last row of the table
    max_score = 0
    for i in range(n+1):
        if dp[i][k] > max_score:
            max_score = dp[i][k]
    return max_score

# Example usage
array = [3, 5, 8, 2, 4, 7, 1, 9, 6, 3, 2]
k = 3
z = 2
print(max_score(array, k, z))
