python
import sys
input = sys.stdin.read

def max_remaining_element(n, a):
    # Initialize the dp array
    dp = [[0] * n for _ in range(n)]
    
    # Base case: when the subarray has only one element
    for i in range(n):
        dp[i][i] = a[i]
    
    # Fill the dp array
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i+1][j] - a[i], dp[i][j-1] - a[j])
    
    # The answer for the whole array
    return dp[0][n-1]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    result = max_remaining_element(n, a)
    print(result)

