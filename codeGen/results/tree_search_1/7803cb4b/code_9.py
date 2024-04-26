def find_min_length(n, a):
    dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1  # Base case: a single element cannot be reduced further
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Case 1: No merging with the first element
            dp[i][j] = 1 + dp[i+1][j]
            # Case 2: Try to merge the first element with some other element
            for k in range(i+1, j+1):
                if a[i] == a[k] and (k == i+1 or dp[i+1][k-1] == 0):
                    dp[i][j] = min(dp[i][j], dp[k+1][j])
    
    return dp[0][n-1]

# Read input from stdin
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Get the answer and print to stdout
print(find_min_length(n, a))
