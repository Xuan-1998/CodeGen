import sys

def min_operations(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # base case: single element
    for i in range(n):
        dp[i][i] = 0

    # fill up the table
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if arr[j] > arr[i]:
                dp[i][j] = 1 + min(dp[k][j-1] for k in range(i, j) if arr[k] <= arr[j])
            else:
                dp[i][j] = dp[i][i+j-1]
    # read off the last row as the solution
    return min(dp[i][-1] for i in range(n))

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

print(min_operations(arr))
