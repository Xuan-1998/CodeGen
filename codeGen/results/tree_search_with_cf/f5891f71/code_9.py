python
def max_remaining_value(n, arr):
    # Initialize the DP table
    dp = [[0] * n for _ in range(n)]
    
    # Base case: when the subarray has only one element
    for i in range(n):
        dp[i][i] = arr[i]
    
    # Fill the DP table
    for length in range(2, n + 1):  # subarray lengths from 2 to n
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i][k] - arr[k + 1] for k in range(i, j))
    
    # The answer is the maximum value for the entire array
    return dp[0][n-1]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_value(n, arr)
    print(result)

