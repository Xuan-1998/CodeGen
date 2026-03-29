import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if arr[j] > arr[i]:
                dp[i][j] = True
            else:
                dp[i][j] = False

    max_length = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                max_length = max(max_length, j - i + 1)

    return max_length

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Call the function and print the result to stdout
print(longest_increasing_subsequence(arr))
