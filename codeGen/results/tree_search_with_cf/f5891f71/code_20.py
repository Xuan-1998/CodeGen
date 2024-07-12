python
def max_remaining_element(n, array):
    # Initialize the dp table with size n x n
    dp = [[0] * n for _ in range(n)]
    
    # Set the base cases: dp[i][i] = a[i] for all i
    for i in range(n):
        dp[i][i] = array[i]
    
    # Fill the dp table
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i+1][j] - array[i], dp[i][j-1] - array[j])
    
    # The result is dp[0][n-1]
    return dp[0][n-1]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    array = list(map(int, data[1:]))
    
    result = max_remaining_element(n, array)
    print(result)

