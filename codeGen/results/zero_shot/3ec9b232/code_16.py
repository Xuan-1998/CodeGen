def count_collections(n, m):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    arrays_in_collection = [0] * (n + 1)

    # Base case: one array with all elements from 1 to n
    dp[0][n] = 1

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if m[j - 1] == i:
                arrays_in_collection[i] += 1
                for k in range(j, n + 1):
                    dp[i][k] = (dp[i][k] + dp[i-1][j-1]) % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][n]

# Example usage
n = int(input())
m = list(map(int, input().split()))
print(count_collections(n, m))
